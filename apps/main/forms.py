from django import forms

from .models import Review, Recipe


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Message'}),
        }
        

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'yields', 'photo', 'cook_time', 'kitchen', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'ingredients': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Инструкция'}),
            'yields': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Доходность'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'cook_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Время готовки (минуты)'}),
            'kitchen': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
