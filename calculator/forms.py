from django import forms
from calculator.models import *


class CalculatorFieldsForm(forms.Form):
    products = forms.ModelChoiceField(queryset=Products.objects.all(), label='Выберите продукт')
    count = forms.IntegerField(label='Введите количество продукта, гр')



