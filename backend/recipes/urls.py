from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DownloadShoppingCart, FavouriteViewSet, IngredientViewSet,
                    RecipesViewSet, ShoppingListViewSet, SubscriptionViewSet,
                    TagViewSet, show_subscription)

V_API = 'v1.0/'
router_v1 = DefaultRouter()

router_v1.register('recipes', RecipesViewSet, basename='recipes')
router_v1.register('tags', TagViewSet)
router_v1.register('ingredients', IngredientViewSet)
router_v1.register('', RecipesViewSet, basename='recipes')


urlpatterns = [
    path(V_API+'users/subscriptions/', show_subscription),
    path(V_API+'users/<int:user_id>/subscribe/', SubscriptionViewSet.as_view()),
    path(V_API+'recipes/<int:recipe_id>/favorite/', FavouriteViewSet.as_view()),
    path(V_API+'recipes/<int:recipe_id>/shopping_cart/', ShoppingListViewSet.as_view()),
    path(V_API+'recipes/download_shopping_cart/', DownloadShoppingCart.as_view()),
    path(V_API, include(router_v1.urls)),
]
