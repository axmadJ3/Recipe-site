# Generated by Django 5.0.7 on 2024-07-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_kitchen_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]