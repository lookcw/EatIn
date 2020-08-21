from django.db import models


class Recipes(models.Model):
    title = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    picture_link = models.TextField(blank=True, null=True)
    name = models.TextField(unique=True, primary_key=True)
    num_ing = models.IntegerField()


class Ingredients(models.Model):
    ingredient = models.TextField(blank=True, null=True)
    quantity = models.TextField(blank=True, null=True)
    name = models.ForeignKey(
        'recipe.Recipes', models.DO_NOTHING, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
