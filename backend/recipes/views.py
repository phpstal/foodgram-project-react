from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django_filters import CharFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import (Recipe, Tag, Ingredient, CustomUser, Subscription,
                     Favorites, ShoppingCart)
from .permissions import IsAdmin, IsAuthor, IsReadOnly
from users.serializers import CustomUserSerializer 
from .serializers import (RecipeSerializer, 
                          TagSerializer,
                          IngredientSerializer,
                          ShowFollowersSerializer,
                          AddFavouriteRecipeSerializer)


class RecipeFilter(FilterSet):
    tags = CharFilter(field_name='tags__slug',
                       lookup_expr='icontains')
    is_favorited = CharFilter(field_name='is_favorited',
                       lookup_expr='icontains')
    is_in_shopping_cart = CharFilter(field_name='is_in_shopping_cart',
                       lookup_expr='icontains')
    author = CharFilter(field_name='author__username',
                       lookup_expr='icontains')

    class Meta:
        model = Recipe
        fields = ['tags', 'is_favorited', 'is_in_shopping_cart', 'author']


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-id')
    #permission_classes = (IsAdmin, IsAuthor, IsReadOnly)
    serializer_class = RecipeSerializer
    #filter_backends = (DjangoFilterBackend, )
    #filterset_class = RecipeFilter
    #def get_serializer_class(self):
    #    if self.request.method == 'GET':
    #        return ShowRecipeSerializer
    #    return CreateRecipeSerializer
    #def get_serializer_context(self):
    #    context = super().get_serializer_context()
    #    context.update({'request': self.request})
    #    return context


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def ShowSubscription(request):
    users = request.user.followers.all()
    user_obj = []
    for follow_obj in users:
        user_obj.append(follow_obj.author)
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(user_obj, request)
    serializer = ShowFollowersSerializer(
        result_page, many=True, context={'current_user': request.user})
    return paginator.get_paginated_response(serializer.data)


class SubscriptionViewSet(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, user_id):
        user = request.user
        author = get_object_or_404(CustomUser, id=user_id)
        if Subscription.objects.filter(user=user, author=author).exists():
            return Response(
                'Вы уже подписаны',
                status=status.HTTP_400_BAD_REQUEST)
        Subscription.objects.create(user=user, author=author)
        serializer = CustomUserSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, user_id):
        user = request.user
        author = CustomUser.objects.get(id=user_id)
        if not Subscription.objects.get(user=user, author=author):
            return Response('Подписки не было',
                            status=status.HTTP_400_BAD_REQUEST)
        Subscription.objects.get(user=user, author=author).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FavouriteViewSet(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if Favorites.objects.filter(user=user, recipe=recipe).exists():
            return Response(
                'Вы уже добавили рецепт в избранное',
                status=status.HTTP_400_BAD_REQUEST)
        Favorites.objects.create(user=user, recipe=recipe)
        serializer = AddFavouriteRecipeSerializer(recipe)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED)

    def delete(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        
        if not Favorites.objects.get(user=user, recipe=recipe):
            return Response('Рецепт не был в избранном',
                            status=status.HTTP_400_BAD_REQUEST)
        Favorites.objects.get(user=user, recipe=recipe).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShoppingListViewSet(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if ShoppingCart.objects.filter(user=user, purchase=recipe).exists():
            return Response(
                'Вы уже добавили рецепт в список покупок',
                status=status.HTTP_400_BAD_REQUEST)
        ShoppingCart.objects.create(user=user, purchase=recipe)
        serializer = AddFavouriteRecipeSerializer(recipe)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED)

    def delete(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        
        if not ShoppingCart.objects.get(user=user, purchase=recipe):
            return Response('Рецепта нет в корзине',
                            status=status.HTTP_400_BAD_REQUEST)
        ShoppingCart.objects.get(user=user, purchase=recipe).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DownloadShoppingCart(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        users_shopping_list_recipes = user.purchases.all()
        recipes = []
        for i in users_shopping_list_recipes:
            recipes.append(i.purchase)
        ingredients = []
        for recipe in recipes:
            ingredients.append(recipe.ingredients.all())
        new_ingredients = []
        for set in ingredients:
            for ingredient in set:
                new_ingredients.append(ingredient)
        ingredients_dict = {}
        for ing in new_ingredients:
            if ing in ingredients_dict.keys():
                ingredients_dict[ing] += ing.quantity
            else:
                ingredients_dict[ing] = ing.quantity
        wishlist = []
        for k, v in ingredients_dict.items():
            wishlist.append(f'{k.name} - {v} {k.unit} \n')
        wishlist.append('\n')
        wishlist.append('FoodGram, 2021')
        response = HttpResponse(wishlist, 'Content-Type: text/plain')
        response['Content-Disposition'] = 'attachment; filename="wishlist.txt"'
        return response