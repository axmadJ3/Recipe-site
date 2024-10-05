from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Recipe, Ingredient, Kitchen, Category, Review

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fields = ['title','slug', 'description', 'ingredients', 'category', 'instructions', 'yields', 'photo', 'cook_time', 'kitchen']
    filter_horizontal = ['ingredients',]
    list_display = ['title', 'category', 'kitchen', 'recipe_photo']
    list_per_page = 5
    
    @admin.display(description='Фото', ordering='content')
    def recipe_photo(self, recipe: Recipe):
        if recipe.photo:
            return mark_safe(f"<img src='{recipe.photo.url}' width='150'>")
        return 'Без фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name','slug', 'photo']
    
    
@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name','slug', 'photo']
    list_per_page = 8
    
    
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_per_page = 10


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe', 'created']
    list_per_page = 5

admin.site.site_header = 'Админка Delicious' 
admin.site.site_title = 'Админка Delicious'
admin.site.index_title = 'Панель управления'
