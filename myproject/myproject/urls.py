# myproject/urls.py
from django.contrib import admin
from django.urls import path, include  # Include the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),  # Ensure this is included
]
