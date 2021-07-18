from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (RecipeViewSet, TagViewSet, IngredientViewSet,
                    ShowFollows, FollowViewSet)


router_v1 = DefaultRouter()
router_v1.register('recipes', RecipeViewSet)
router_v1.register('tags', TagViewSet)
router_v1.register('ingredients', IngredientViewSet)


urlpatterns = [
    path('users/subscriptions/', ShowFollows),
    path('users/<user_id>/subscribe/', FollowViewSet.as_view()),
    path('', include(router_v1.urls)),
]
