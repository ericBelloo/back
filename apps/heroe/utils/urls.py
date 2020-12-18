
# Django
from django.urls import path
# Models
from apps.heroe.utils.views import create_heroes

app_name = 'utils_heroe'

urlpatterns = [
    path('create-heroes/', create_heroes, name='create_heroes'),
]
