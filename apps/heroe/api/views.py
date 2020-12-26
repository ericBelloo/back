
# Rest Framework
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
# Serializers
from apps.heroe.api.serializers import HeroesListSerializer, HeroeDetailSerializer
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
    serializer_class = HeroesListSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Heroes.objects.all()


class HeroeDetail(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Heroes.objects.get(pk=pk)
        except Heroes.DoesNotExist:
            raise Http404

    def get(self, request):
        heroe = self.get_object(request.GET.get('pk'))
        heroe_serializer = HeroeDetailSerializer(heroe)
        return Response(data=heroe_serializer.data, status=status.HTTP_200_OK)


