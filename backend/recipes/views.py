from .models import Recipe
from rest_framework import viewsets

from .serializers import RecipeSerializer


#PERMISSION_CLASSES = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer