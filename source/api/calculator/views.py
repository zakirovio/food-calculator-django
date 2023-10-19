from rest_framework import generics
from django.shortcuts import render
from django.views import generic
from apps.calculator.utils import CommonData, count_cart_data
from apps.calculator import forms
import json
from apps.calculator import models
from api.calculator import serializers
from api.calculator import pagination


# WEB
class CalculatorHome(generic.FormView, CommonData):
    template_name = "calculator/index.html"
    form_class = forms.CalculatorFieldsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_common_context(title="Главная калькулятор")

        if self.request.POST:
            qd = dict(self.request.POST)
            js_string = [item for item in qd.keys()][0]
            products_list = json.loads(js_string)
            values = count_cart_data(data=products_list)
            print(values)
            context['values'] = values

        return dict(list(context.items()) + list(user_context.items()))


class ShowCategory(CommonData, generic.ListView):
    model = models.Products
    template_name = 'calculator/category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_title = models.Categories.objects.get(slug=self.kwargs['slug'])
        extra_context = self.get_common_context(title=category_title, selected=1)

        return dict(list(context.items()) + list(extra_context.items()))

    def get_queryset(self):
        return models.Products.objects.select_related("category").filter(category__slug=self.kwargs['slug'])


def about(request):
    return render(request=request, template_name='about.html')


def show_articles(request):
    ...


# API
class CategoriesList(generics.ListAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer


class ProductsList(generics.ListAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    pagination_class = pagination.ProductsListPagination


class ProductsListByCategory(generics.ListAPIView):
    serializer_class = serializers.ProductsSerializer
    pagination_class = pagination.ProductsListPagination

    def get_queryset(self):
        category = self.kwargs.get('category')
        queryset = models.Products.objects.filter(category_id=category)
        return queryset
