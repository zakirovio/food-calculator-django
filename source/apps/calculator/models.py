from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




class Products(models.Model):
    category_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    calories = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
