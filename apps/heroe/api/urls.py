

from django.urls import path
from apps.heroe.api.views import HeroesList

app_name = 'heroe_api'

urlpatterns = [
    path('heroes-list/', HeroesList.as_view(), name='get_heroes_list'),
]