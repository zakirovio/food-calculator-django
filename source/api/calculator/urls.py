from api.calculator.views import CategoriesList, CategoryDetail, ProductsList, ProductsListByCategory
from django.urls import path, include

urlpatterns = [
    path('categories/', CategoriesList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('products/', ProductsList.as_view()),
    path('products/category/<int:category>/', ProductsListByCategory.as_view()),

]
