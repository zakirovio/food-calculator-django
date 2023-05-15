from django.shortcuts import render, redirect
from calculator.models import *
from django.views.generic import ListView, TemplateView, CreateView
from calculator.utils import CommonData, menu, categories_list
from calculator.utils import *
from calculator.forms import *


def CalculatorHome(request):
    context = {
        'menu': menu,
        'title': 'Главная | Калькулятор',
        'categories_list': categories_list,
        'selected': 1
    }

    if request.method == 'POST':
        form = CalculatorFieldsForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data.get('products')
            weight_coeff = form.cleaned_data.get('count') / 100
            values = [product.calories, product.protein, product.fats, product.carbs]
            food_values = count_food_values(*values, coeff=weight_coeff)
            context['food_values'] = food_values
            context['form'] = form

            return render(request=request, template_name='calculator/index.html', context=context)
    else:
        form = CalculatorFieldsForm()
        context['form'] = form
        return render(request=request, template_name='calculator/index.html', context=context)


class ShowCategory(CommonData, ListView):
    model = Products
    template_name = 'calculator/category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_title = Categories.objects.get(slug=self.kwargs['slug'])
        extra_context = self.get_common_context(title=category_title)

        return dict(list(context.items()) + list(extra_context.items()))

    def get_queryset(self):
        return Products.objects.filter(category__slug=self.kwargs['slug'])


def about(request):
    ...


def show_articles(request):
    ...
