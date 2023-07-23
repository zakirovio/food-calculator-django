from calculator.models import *

categories_list = Categories.objects.all()
menu = [
    {'title': 'Категории продуктов | Таблицы', 'select_id': 1, 'path_name': 'home'},
    # Other points
]


def count_cart_data(data: dict) -> dict:
    calories = 0
    protein = 0
    fats = 0
    carbs = 0

    for item in data:
        product_id = item['id']
        count = int(item['count'])
        factor = count / 100
        product = Products.objects.get(id=product_id)
        calories += (product.calories * factor)
        protein += (product.protein * factor)
        fats += (product.fats * factor)
        carbs += (product.carbs * factor)

    return {'calories': calories, 'protein': protein, 'fats': fats, 'carbs': carbs}


class CommonData:
    def get_common_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['categories_list'] = categories_list

        if 'selected' not in context:
            context['selected'] = 0
        return context
