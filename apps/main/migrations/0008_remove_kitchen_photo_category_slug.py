# Generated by Django 5.0.7 on 2024-07-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_kitchen_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitchen',
            name='photo',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
