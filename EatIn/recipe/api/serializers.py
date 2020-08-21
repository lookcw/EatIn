from rest_framework import serializers

from recipe.models import Recipes,Ingredients

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('name','title','instructions','picture_link')

class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingredients 
        fields = ('name','ingredient','quantity')