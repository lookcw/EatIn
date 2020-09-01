from recipe.models import Recipes, Ingredients
from .serializers import RecipeSerializer, IngredientSerializer
from django.db.models import Count, Q
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .parse_ingredients import parse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

import json


def _consolidate_recipes(recipes):
    ing_list = Ingredients.objects.filter(
        name_id__in=[recipe['name'] for recipe in recipes]).values()
    recipes = {recipe['name']: recipe for recipe in recipes}
    for recipe in recipes:
        recipes[recipe]['ingredients'] = []
    for ing in ing_list:
        recipes[ing['name_id']]['ingredients'].append({'ingredient': ing['ingredient'],
                                                       'quantity': ing['quantity']})
    return [recipes[name] for name in recipes]


def all_recipes(request):
    recipes = Recipes.objects.values()
    return JsonResponse(_consolidate_recipes(recipes), safe=False)


def slice_recipes(request):
    start, count = int(request.GET['start']), int(request.GET['count'])
    recipes = Recipes.objects.values()
    return JsonResponse(_consolidate_recipes(recipes)[start:start + count], safe=False)


@csrf_exempt
def ing_query(request):
    req = json.loads(request.body)['data']
    start, end, ing_arr = req['start'], req['end'], req['ing_arr']
    counts = list(Ingredients.objects.filter(ingredient__in=ing_arr).values(
        'name').annotate(num_ing=Count('name')).values('name_id', 'num_ing'))
    for count in counts:
        count['req_ing'] = getattr(Recipes.objects.get(
            name=count['name_id']), 'num_ing')
    found_names = [count['name_id']
                   for count in counts if count['num_ing'] == count['req_ing']]
    recipes = list(Recipes.objects.filter(name__in=found_names).values())
    return JsonResponse(_consolidate_recipes(recipes)[start:end], safe=False)
