from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.product_search, name='product_search'),
]