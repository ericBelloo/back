
from django.urls import path
from apps.heroe.views import HeroesList, HeroeDetail

app_name = 'heroe'

urlpatterns = [
    path('heroes-list/', HeroesList.as_view(), name='get_heroes_list'),
    path('heroe/', HeroeDetail.as_view(), name='get_heroe'),
]
