from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet


router_v1 = DefaultRouter()
router_v1.register('recipes', RecipeViewSet)


urlpatterns = [
    path('', include(router_v1.urls))
]
