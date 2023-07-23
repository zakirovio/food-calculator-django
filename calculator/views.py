from django.shortcuts import render, redirect
from calculator.models import *
from django.views.generic import ListView, TemplateView, CreateView
from calculator.utils import CommonData, menu, categories_list
from calculator.utils import *
from calculator.forms import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import json


def CalculatorHome(request):
    context = {
        'menu': menu,
        'title': 'Главная | Калькулятор',
        'categories_list': categories_list,
        'selected': 1
    }
    
    form = CalculatorFieldsForm()
    context['form'] = form
    if request.POST:
        qd = dict(request.POST)
        js_string = [item for item in qd.keys()][0]
        products_list = json.loads(js_string)  # нужно распарсить 
        values = count_cart_data(data=products_list)
        print(values)
        context['values'] = values
 
    return render(request=request, template_name='calculator/index.html', context=context)


class ShowCategory(CommonData, ListView):
    model = Products
    template_name = 'calculator/category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_title = Categories.objects.get(slug=self.kwargs['slug'])
        extra_context = self.get_common_context(title=category_title, selected=1)

        return dict(list(context.items()) + list(extra_context.items()))

    def get_queryset(self):
        return Products.objects.filter(category__slug=self.kwargs['slug'])


def about(request):
    return render(request=request, template_name='about.html')


def show_articles(request):
    ...
