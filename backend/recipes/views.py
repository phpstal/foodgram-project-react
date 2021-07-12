from .models import Recipe
from rest_framework import viewsets

from .serializers import RecipeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer