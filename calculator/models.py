from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


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


