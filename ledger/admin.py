from django.contrib import admin

from . models import Recipe, RecipeIngredient, Ingredients, RecipeImage

class TaskInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        TaskInLine,
    ]

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage

    fieldsets = [
        ("Details", 
         {'fields':[
             ('recipe_image', 'description'), 
             'recipe'
             ]
                     })
    ]

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)   
admin.site.register(RecipeImage, RecipeImageAdmin)