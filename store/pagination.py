from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 10          # عدد المنتجات في كل صفحة
    page_size_query_param = 'page_size'  # العميل يغير العدد
    max_page_size = 100     # أقصى عدد
