from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField()

def __str__(self):
    return self.name
