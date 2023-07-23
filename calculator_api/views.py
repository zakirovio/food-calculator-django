from rest_framework import generics

from calculator.models import Categories, Products
from calculator_api.serializers import CategoriesSerializer, ProductsSerializer
from calculator_api.pagination import ProductsListPagination


class CategoriesList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class ProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = ProductsListPagination


class ProductsListByCategory(generics.ListAPIView):
    serializer_class = ProductsSerializer
    # pagination_class = ProductsListPagination

    def get_queryset(self):
        category = self.kwargs.get('category')
        queryset = Products.objects.filter(category_id=category)
        return queryset
