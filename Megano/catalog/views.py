import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Review, Tag, Category
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    TagSerializer,
)


@api_view(['GET'])
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def catalog(request):
    category_id = request.GET.get('category', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    products = Product.objects.all()
    if category_id is not None:
        products = products.filter(category=category_id)

    if min_price is not None:
        products = products.filter(price__gte=min_price)

    if max_price is not None:
        products = products.filter(price__lte=max_price)
    serializer = ProductSerializer(products, many=True, context={'request': request})
    data = {"items": serializer.data}
    return Response(data)


@api_view(['GET'])
def catalog_popular(request):
    popular_products = Product.objects.filter(rating__isnull=False).order_by('-rating')

    serializer = ProductSerializer(popular_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def catalog_limited(request):
    limit = int(request.GET.get('limit', 10))

    products = Product.objects.filter(count__lte=limit)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sales(request):
    products_with_sale = Product.objects.filter(salePrice__gt=0)

    serializer = ProductSerializer(products_with_sale, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def banners(request):
    banner_products = Product.objects.filter(is_banner_product=True)

    serializer = ProductSerializer(banner_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def tag_list(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)


@api_view(['POST'])
def product_review(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    data = {"product": product.id, **request.data}
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        reviews = Review.objects.filter(product=product)
        total_rating = sum(review.rate for review in reviews)
        product.rating = total_rating / max(reviews.count(), 1)
        product.save(update_fields=['rating'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
