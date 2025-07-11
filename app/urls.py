# app/urls.py

from django.urls import path
from .views import dashboard, product_detail

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]
