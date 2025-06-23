from django.urls import path
from .views import *

urlpatterns = [
    path('add/', requisition_create, name='requisition_create'),
    path('', requisition_list, name='requisition_list'),
    path('admin/', requisition_admin_list, name='requisition_admin_list'),
    path('approve/<int:pk>/', approve_requisition, name='approve_requisition'),
    path('reject/<int:pk>/', reject_requisition, name='reject_requisition'),
]