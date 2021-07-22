from django_filters import CharFilter, FilterSet

from .models import Recipe


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
