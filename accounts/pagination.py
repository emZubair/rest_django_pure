from rest_framework.pagination import PageNumberPagination


class PureRestPagination(PageNumberPagination):
    page_size = 4
