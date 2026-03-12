from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

# Create your views here.
def recipes_list(request):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes,
    }

    return render(request, 'recipes_list.html', ctx)

def recipes_detail(request, pk):
    ctx = {
        "recipe": Recipe.objects.get(pk=pk)
    }

    return render(request, 'recipes_details.html', ctx)

def recipe_add(request):
    form = RecipeForm()

    ctx = {
        "form": form
    }

    if request.method== 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
    return render(request, 'recipe_add.html', ctx)

def recipe_add_image(request):
    form = RecipeImageForm()

    ctx = {
        "form": form
    }

    if request.method== 'POST':
        form = RecipeImageForm(request.POST)
        if form.is_valid():
            image = form.save()
    return render(request, 'recipe_add_image.html', ctx)

class RecipeDetailView(LoginRequiredMixin,DetailView):
    model = Recipe
    template_name = "recipe_details.html"

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe_add.html'
    form_class = RecipeForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipes-list')

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'recipe_add_image.html'
    form_class = RecipeImageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.get(pk = self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', 
                            kwargs={'pk': self.object.recipe.pk })


