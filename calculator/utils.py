from calculator.models import *


categories_list = Categories.objects.all()
menu = [
    {'title': 'Главная | Калькулятор', 'select_id': 1, 'path_name': 'home'},
    {'title': 'Категории продуктов', 'select_id': 2, 'path_name': 'home'},
    {'title': 'Статьи', 'select_id': 3, 'path_name': 'articles'},
    {'title': 'О сайте', 'select_id': 4, 'path_name': 'about'}
]


def count_food_values(*args, coeff) -> tuple:
    calories, protein, fat, carbs = args

    calories = coeff * calories
    protein = coeff * protein
    fat = coeff * fat
    carbs = coeff * carbs

    return calories, protein, fat, carbs


class CommonData:
    def get_common_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['categories_list'] = categories_list

        if 'selected' not in context:
            context['selected'] = 0
        return context
