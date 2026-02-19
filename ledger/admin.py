from django.contrib import admin
from . models import Recipe, RecipeIngredient

class TaskInLine(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [
        TaskInLine,
    ]


# Register your models here.
admin.site.register(Recipe, RecipeAdmin)