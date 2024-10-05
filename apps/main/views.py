from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Recipe, Category, Kitchen
from .forms import ReviewForm, RecipeForm

def home(request):
    dishes = Recipe.objects.all()

    context = {
        'dishes': dishes,
        'range': range(1, 7 + 1)
    }
    return render(request, 'main/home.html', context=context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    category = recipe.category  
    kitchen = recipe.kitchen
    reviews = recipe.reviews.all()  # Фильтруем отзывы по рецепту
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.user = request.user
            review.save()
            return redirect('recipe_detail', slug=recipe.slug)
    else:
        form = ReviewForm()
        
    data = {
        'recipe': recipe,
        'category': category,
        'kitchen': kitchen,
        'reviews': reviews, 
        'form': form
    }
    
    return render(request, 'main/recipe_detail.html', context=data)


def category(request):
    categories = Category.objects.all()
    kitchens = Kitchen.objects.all()
    
    data = {
        'categories': categories,
        'kitchens': kitchens
    }
    return render(request, 'main/category.html', context=data)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    recipes = category.recipes.all()  
    data = {
        'category': category,
        'recipes': recipes
    }
    return render(request, 'main/category_detail.html', context=data)


def kitchen_detail(request, slug):
    kitchen = get_object_or_404(Kitchen, slug=slug)
    recipes = kitchen.recipes.all()  
    data = {
        'kitchen': kitchen,
        'recipes': recipes
    }
    return render(request, 'main/kitchen_detail.html', context=data)
    
    
def search_recipes(request):
    query = request.GET.get('query')
    recipes = Recipe.objects.filter(title__icontains=query)
    data = {
        'recipes': recipes, 
        'query': query
        }
    return render(request, 'main/search_results.html', context=data)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes_view')  
    else:
        form = RecipeForm()
    
    data = {
        'form': form
    }
    return render(request, 'main/create_recipe.html', context=data)


def about(request):
    return render(request, 'main/about.html')