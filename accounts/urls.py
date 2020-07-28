from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from digifix_computer_repair import settings
from . views import home_view, LoginView, RegisterUser, DashboardView, UpdateAccountSettings
import django.contrib.auth.views as AuthViews


urlpatterns = [
    path('', home_view, name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', AuthViews.LogoutView.as_view(), name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('settings', UpdateAccountSettings.as_view(), name='settings'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
