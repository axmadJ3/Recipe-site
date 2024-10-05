from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from unidecode import unidecode
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Ingredient(models.Model):
    class Meta:
        verbose_name = "Ингридиент"  
        verbose_name_plural = "Ингридиенты"  
        
        
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Kitchen(models.Model):
    class Meta:
        verbose_name = "Кухня"  
        verbose_name_plural = "Кухни"  
        
        
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    photo = models.ImageField(upload_to='category/', blank=True, verbose_name='Фото')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(unidecode(self.title))
            slug = original_slug
            counter = 1
            
            while Recipe.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            
            self.slug = slug
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    class Meta:
        verbose_name = "Категория"  
        verbose_name_plural = "Категории" 
        
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    photo = models.ImageField(upload_to='category/', blank=True, verbose_name='Фото')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(unidecode(self.title))
            slug = original_slug
            counter = 1
            
            while Recipe.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            
            self.slug = slug
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    
class Recipe(models.Model):
    class Meta:
        verbose_name = "Рецепт"  
        verbose_name_plural = "Рецепты" 
        
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = RichTextField(verbose_name='Описание')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Ингридиенты')
    instructions = RichTextField(verbose_name='Инструкция')
    yields = models.PositiveIntegerField(verbose_name='Доходность', blank=True, null=True)
    photo = models.ImageField(upload_to='uploads/', blank=True, verbose_name='Фото')
    cook_time = models.PositiveIntegerField(verbose_name='Время готовки в минутах')
    kitchen = models.ForeignKey(Kitchen, related_name='recipes', on_delete=models.CASCADE, verbose_name='Кухня') 
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(unidecode(self.title))
            slug = original_slug
            counter = 1
            
            while Recipe.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            
            self.slug = slug
        
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = "Отзыв"  
        verbose_name_plural = "Отзывы" 
        
        
    recipe = models.ForeignKey('Recipe', related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Отзыв пользователя {self.user.username} на рецепт {self.recipe.title}'