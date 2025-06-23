from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', product_create, name='product_create'),
    path('edit/<int:pk>/', product_update, name='product_update'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
]
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)