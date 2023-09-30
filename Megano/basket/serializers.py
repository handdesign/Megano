from rest_framework import serializers

from catalog.serializers import ProductSerializer
from .models import Order, Basket


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_products(self, order):
        product_data = []
        for product in order.products.all():
            product_data.append({
                'id': product.id,
                'title': product.title,
                'price': product.price,
                'salePrice': product.salePrice,
                'images': product.images.url if product.images else None,
            })
        return product_data


class BasketSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Basket
        fields = '__all__'
