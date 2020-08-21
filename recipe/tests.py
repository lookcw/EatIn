from django.test import TestCase
from recipe.models import Recipes, Ingredients
from recipe.api.views import all_recipes, ing_query
from unittest.mock import MagicMock
from django.test.client import RequestFactory
from django.http import JsonResponse
import json


# Create your tests here.


ING_1 = {'ingredient': 'ing 1', 'quantity': '1'}
ING_2 = {'ingredient': 'ing 2', 'quantity': '1'}
ING_3 = {'ingredient': 'ing 3', 'quantity': '1'}


RECIPE_1 = {'title': '1',
            'instructions': 'instruction 1',
            'picture_link': 'picture_link 1',
            'name': 'name 1',
            'num_ing': 2,
            'ingredients': [ING_1, ING_2]}

RECIPE_2 = {'title': '2',
            'instructions': 'instruction 2',
            'picture_link': 'picture_link 2',
            'name': 'name 2',
            'num_ing': 2,
            'ingredients': [ING_1, ING_3]}


class RecipeTestCase(TestCase):
    def setUp(self):
        self.rf = RequestFactory()
        Recipes.objects.create(**RECIPE_1)
        Recipes.objects.create(**RECIPE_2)
        ing_12 = dict(
            ING_1, **{'id': 11, 'name': Recipes.objects.get(pk='name 1')})
        ing_21 = dict(
            ING_2, **{'id': 21, 'name': Recipes.objects.get(pk='name 1')})
        ing_22 = dict(
            ING_1, **{'id': 22, 'name': Recipes.objects.get(pk='name 2')})
        ing_32 = dict(
            ING_3, **{'id': 32, 'name': Recipes.objects.get(pk='name 2')})
        Ingredients.objects.create(**ing_12)
        Ingredients.objects.create(**ing_21)
        Ingredients.objects.create(**ing_22)
        Ingredients.objects.create(**ing_32)

    def test_get_all_recipes(self):
        get_req = self.rf.get('/hello/')
        self.assertJSONEqual(all_recipes(get_req).content,
                             [RECIPE_1, RECIPE_2])

    def test_query_recipes(self):
        body_1 = {'data':
                  {'start': 0,
                   'end': 3,
                   'ing_arr': ['ing 1', 'ing 2']}}
        body_2 = {'data':
                  {'start': 0,
                   'end': 3,
                   'ing_arr': ['ing 1', 'ing 3']}}
        both_body = {'data': {'start': 0,
                              'end': 3,
                              'ing_arr': ['ing 1', 'ing 2', 'ing 3']}}
        limited_body = {'data':
                        {'start': 0,
                         'end': 1,
                         'ing_arr': ['ing 1', 'ing 2', 'ing 3']}}
        req_1 = self.rf.post('', body_1, content_type='application/json')
        req_2 = self.rf.post('', body_2, content_type='application/json')
        req_3 = self.rf.post('', both_body, content_type='application/json')
        req_4 = self.rf.post('', limited_body, content_type='application/json')
        self.assertJSONEqual(ing_query(req_1).content, [RECIPE_1])
        self.assertJSONEqual(ing_query(req_2).content, [RECIPE_2])
        self.assertJSONEqual(ing_query(req_3).content, [RECIPE_1, RECIPE_2])
        json_4 = json.loads(ing_query(req_4).content)
        self.assertEqual(len(json_4), 1)
        self.assertIn(json_4[0], [RECIPE_1, RECIPE_2])
