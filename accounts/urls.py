from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
     path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)