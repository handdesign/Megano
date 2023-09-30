from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'catalog_items'

urlpatterns = [
    path('api/categories/', categories_list, name='categories-list'),
    path('api/catalog/', catalog, name='catalog'),
    path('api/products/popular', catalog_popular, name='catalog-popular'),
    path('api/products/limited', catalog_limited, name='catalog-limited'),
    path('api/sales/', sales, name='sales'),
    path('api/banners/', banners, name='banners'),
    path('api/tags/', tag_list, name='tag-list'),
    path('api/product/<int:id>/', product_detail, name='product_detail'),
    path('api/product/<int:id>/review/', product_review, name='product_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
