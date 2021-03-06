
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from back import settings

urlpatterns = [
    # django urls
    path('admin/', admin.site.urls),
    # heroe api
    path('heroes/', include('apps.heroe.urls')),
    # heroe utils
    path('utils/heroes/', include('apps.heroe.utils.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
