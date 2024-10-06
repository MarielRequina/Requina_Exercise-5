# api/urls.py
from django.urls import path
from .views import CategoryListCreateView

urlpatterns = [
    path('api/articles/categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]
