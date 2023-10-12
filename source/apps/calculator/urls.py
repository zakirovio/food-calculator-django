from django.urls import path
from api.calculator.views import CalculatorHome, ShowCategory, show_articles, about

urlpatterns = [
    path('', CalculatorHome.as_view(), name='home'),
    path('category/<slug:slug>/', ShowCategory.as_view(), name='category'),
    path('articles/', show_articles, name='articles'),
    path('about/', about, name='about')
]
