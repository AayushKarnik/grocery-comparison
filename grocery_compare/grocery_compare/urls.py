# grocery_compare/urls.py
from django.contrib import admin
from django.urls import path, include
from groceries import views as grocery_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', grocery_views.home, name='home'),  # Homepage URL
    path('groceries/', include('groceries.urls')),  # Include app URLs
]
