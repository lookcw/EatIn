from django.urls import path
from .views import all_recipes, ing_query, slice_recipes

urlpatterns = [
    path('allrecipes', all_recipes, name='allrecipes'),
    path('ing_query', ing_query, name='ing_query'),
    path('slicerecipes', slice_recipes, name='slice_recipes'),
]
