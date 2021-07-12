from django.urls import path

from .views import PostViewSet


urlpatterns = [
    path('recipes/', PostViewSet),
]
