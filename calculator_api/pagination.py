from rest_framework import pagination


class ProductsListPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100
