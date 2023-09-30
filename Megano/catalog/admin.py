from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", 'title', 'price', 'description', 'rating'
    list_display_links = 'pk', 'title'
