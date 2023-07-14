from django.contrib import admin
from calculator.models import Categories, Products


# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'calories', 'protein', 'fats', 'carbs')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']



