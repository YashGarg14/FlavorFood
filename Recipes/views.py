from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from django.shortcuts import render, get_object_or_404

# Create your views here.

def recipes(request):
    queryset = Recipe.objects.all().order_by('-id')

    if request.GET.get('search'):
        queryset = queryset.filter(title__icontains = request.GET.get('search'))

    context = {'recipes' : queryset}
    return render(request, "recipes.html", context)

def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == "POST":

        data = request.POST
        title = data.get('title')
        description = data.get('description')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')
        time_to_cook = data.get('time_to_cook')

        recepie_image = request.FILES.get('recepie_image')

        Recipe.objects.create(
            title = title,
            description = description, 
            ingredients = ingredients,
            instructions = instructions,
            time_to_cook = time_to_cook,
            recepie_image = recepie_image,
            user=request.user,
        )
        return redirect('/list_recipe')

    return render(request, "add_recipe.html")

@login_required
def list_recipe(request):
    user = request.user
    user_recipes = Recipe.objects.filter(user=user)

    context = {
        'user': user,
        'user_recipes': user_recipes,
    }
    return render(request, 'list_recipe.html', context)

@login_required
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('list_recipe')

@login_required
def update_recipe(request, id):
    
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')
        time_to_cook = data.get('time_to_cook')

        recepie_image = request.FILES.get('recepie_image')

        queryset.title = title
        queryset.description = description
        queryset.ingredients = ingredients
        queryset.instructions = instructions
        queryset.time_to_cook = time_to_cook
        if recepie_image:
            queryset.recepie_image = recepie_image
        queryset.save()
        return redirect('list_recipe')

    
    context = {'recipes' : queryset}
    return render(request, "update_recipe.html", context)
