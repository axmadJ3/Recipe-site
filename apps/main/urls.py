from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='recipes_view'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('category/', views.category, name='category'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('kitchen/<slug:slug>/', views.kitchen_detail, name='kitchen_detail'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('create/', views.create_recipe, name='create_recipes'),
    path('about/', views.about, name='about'),
    
]