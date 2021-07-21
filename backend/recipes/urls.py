from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DownloadShoppingCart, FavouriteViewSet, IngredientViewSet,
                    RecipesViewSet, ShoppingListViewSet, ShowSubscription,
                    SubscriptionViewSet, TagViewSet)

router_v1 = DefaultRouter()

router_v1.register('recipes', RecipesViewSet, basename='recipes')
router_v1.register('tags', TagViewSet)
router_v1.register('ingredients', IngredientViewSet)
router_v1.register('', RecipesViewSet, basename='recipes')


urlpatterns = [
    path('users/subscriptions/', ShowSubscription),
    path('users/<user_id>/subscribe/', SubscriptionViewSet.as_view()),
    path('recipes/<recipe_id>/favorite/', FavouriteViewSet.as_view()),
    path('recipes/<recipe_id>/shopping_cart/', ShoppingListViewSet.as_view()),
    path('recipes/download_shopping_cart/', DownloadShoppingCart.as_view()),
    path('', include(router_v1.urls)),
]
