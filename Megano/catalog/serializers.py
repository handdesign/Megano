from rest_framework import serializers
from .models import (
    Category,
    Subcategory,
    Product,
    Review,
    Specification,
    Tag,
)


class CategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'salePrice', 'images']

    def get_images(self, product):
        images_list = []
        if product.images:
            images_list.append({
                'src': product.images.url,
                'alt': product.title,
            })
        return images_list


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
