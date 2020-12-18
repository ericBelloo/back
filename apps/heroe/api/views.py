
# Rest Framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
# Serializers
from apps.heroe.api.serializers import HeroesSerializer
# Models
from apps.heroe.models import Heroes


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class HeroesList(ListAPIView):
    serializer_class = HeroesSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Heroes.objects.all()