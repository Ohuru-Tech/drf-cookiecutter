from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class DynamicPageSizePagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = getattr(settings, "MAX_PAGE_SIZE")
