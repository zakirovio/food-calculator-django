from django import forms
from calculator.models import *
from calculator.utils import categories_list

class CalculatorFieldsForm(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=categories_list, required=True, empty_label='Выберите категорию', widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'category-select',
            },
        )
    )   
    count = forms.IntegerField(required=True,  widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите количество продукта, гр.', 'id': 'counter'}
    )
        )
