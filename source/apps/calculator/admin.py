from django.contrib import admin
from apps.calculator import models


# Register your models here.
@admin.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'calories', 'protein', 'fats', 'carbs')
    ordering = ['id']


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    ordering = ['id']



