from django.contrib import admin
from .models import FlowerType, Flower

@admin.register(FlowerType)
class FlowerTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'color', 'price')
    list_filter = ('type', 'color')
    search_fields = ('name', 'type__name')
