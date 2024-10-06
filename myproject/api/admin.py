# api/admin.py
from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # You can specify which fields to display in the list view

# Alternatively, you can just use:
# admin.site.register(Category)
