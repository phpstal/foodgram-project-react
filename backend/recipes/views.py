from rest_framework import viewsets
from django_filters import CharFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Recipe, Tag, Ingredient
from .permissions import IsAdmin, IsAuthor, IsReadOnly
from .serializers import (RecipeSerializer, 
                          TagSerializer,
                          IngredientSerializer)


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
    queryset = Recipe.objects.all()
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