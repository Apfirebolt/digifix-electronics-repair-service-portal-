from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from digifix_computer_repair import settings
from . views import home_view


urlpatterns = [
    path('', home_view, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
