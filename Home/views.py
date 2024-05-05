from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Recipes.models import Recipe
# Create your views here.

def home(request):
    queryset = Recipe.objects.all().order_by('-id')[:4]

    total_recipes = Recipe.objects.count()
    random_recipes = Recipe.objects.order_by('?')[:4]

    context = {
        'recipes': queryset,
        'random_recipes': random_recipes
    }

    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Username or password')
            return redirect('home')
        else:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('list_recipe')

    return render(request, 'home/index.html')




def logout_page(request):
    logout(request)
    messages.success(request, 'Logged out.')
    return redirect('home')




def register_page(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        print("Form Data:")
        print("Username:", username)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)
        print("Password:", password)
        print("Confirm Password:", confirm_password)

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('home')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('home')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        messages.success(request, 'Account created successfully. Please Login')
        return redirect('home')

    return render(request, 'home/index.html')