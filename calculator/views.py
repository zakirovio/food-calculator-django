from django.shortcuts import render, redirect
from calculator.models import *
from django.views.generic import ListView, TemplateView, CreateView
from calculator.utils import CommonData, menu, categories_list
from calculator.utils import *
from calculator.forms import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache


def CalculatorHome(request):
    context = {
        'menu': menu,
        'title': 'Главная | Калькулятор',
        'categories_list': categories_list,
        'products': Products.objects.all(),
        'selected': 1
    }

    if request.method == 'POST':
        form = CalculatorFieldsForm(request.POST)
        result = ResultForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # add product to session data
            if form.cleaned_data.get('products'):
                # Temp data
                added_id = form.cleaned_data.get('products').pk
                added_weight = form.cleaned_data.get('count')
                added_name = form.cleaned_data.get('products').title
                data_dict = {'id': added_id, 'title': added_name, 'count': added_weight}
                request.session[added_id] = data_dict
                context['form'] = form
                return redirect('home')
        if result.is_valid():
            if result.cleaned_data.get('result'):
                cart_items = dict(request.session)
                values = count_cart_data(cart_items)
                context['values'] = values
                context['form'] = form
                request.session.clear()
                return render(request=request, template_name='calculator/index.html', context=context)

    form = CalculatorFieldsForm()
    result = ResultForm()
    context['form'] = form
    context['result'] = result
    cart_items = dict(request.session)
    context['cart_items'] = cart_items
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
