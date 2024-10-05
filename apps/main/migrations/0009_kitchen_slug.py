# Generated by Django 5.0.7 on 2024-07-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_kitchen_photo_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]