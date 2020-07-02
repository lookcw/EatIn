from recipe.models import Recipe
from .serializers import RecipeSerializer

from rest_framework.generics import ListAPIView,RetrieveAPIView

class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetailView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
