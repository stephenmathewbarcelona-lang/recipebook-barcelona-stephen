from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from useraccounts.models import Profile


# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Profile, 
                               on_delete=models.CASCADE, 
                               related_name='recipes')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredients, 
                                   on_delete=models.CASCADE, 
                                   related_name='recipe'
                                   )
    recipe = models.ForeignKey(Recipe, 
                               on_delete=models.CASCADE, 
                               related_name='ingredients'
                               )
    
class RecipeImage(models.Model):
    recipe_image = models.ImageField(upload_to='images/', null = False)
    description = models.CharField(max_length = 255)
    recipe = models.ForeignKey(Recipe, 
                               on_delete=models.CASCADE, 
                               related_name='images'
                               )
    
    def __str__(self):
        return self.description