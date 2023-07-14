from django import forms
from calculator.models import *


class CalculatorFieldsForm(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=Categories.objects.all(), required=True, empty_label='Выберите категорию', widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'category-select'
            },
        )
    )

    count = forms.IntegerField(required=True,  widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите количество продукта, гр.'}
    )
        )


class ResultForm(forms.Form):
    # Hidden input to execute calculation
    result = forms.CharField(max_length=255, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'hidden', 'value': 1}
    )
                             )