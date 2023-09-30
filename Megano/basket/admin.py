from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "pk", 'fullName', 'address'
    list_display_links = 'pk', 'fullName'

    def get_product_count(self, obj):
        return obj.products.count()

    get_product_count.short_description = 'Product Count'
