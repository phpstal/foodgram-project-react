from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (RecipeViewSet, TagViewSet, IngredientViewSet,
                    ShowSubscription, SubscriptionViewSet, FavouriteViewSet)


router_v1 = DefaultRouter()

router_v1.register('recipes', RecipeViewSet)
router_v1.register('tags', TagViewSet)
router_v1.register('ingredients', IngredientViewSet)
router_v1.register('', RecipeViewSet)


urlpatterns = [
    path('users/subscriptions/', ShowSubscription),
    path('users/<user_id>/subscribe/', SubscriptionViewSet.as_view()),
    path('recipes/<recipe_id>/favorite/', FavouriteViewSet.as_view()),
    path('', include(router_v1.urls)),
]
