from django.urls import path
from calculator.views import *

urlpatterns = [
    path('', CalculatorHome, name='home'),
    path('category/<slug:slug>/', ShowCategory.as_view(), name='category'),
    path('articles/', show_articles, name='articles'),
    path('about/', about, name='about')
]
