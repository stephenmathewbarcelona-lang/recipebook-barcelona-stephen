from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Recipe 

# Create your views here.

def recipes_list(request):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }
    return render(request, 'recipes_list.html', ctx)

def recipes_detail(request, pk):
    ctx = {
        "recipe": Recipe.objects.get(pk=pk)
    }

    return render(request, 'recipes_details.html', ctx)

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_details.html"

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"