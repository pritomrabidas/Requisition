from django.urls import path
from .views import checkout, order_detail

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
]
