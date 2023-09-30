from django.urls import path
from .views import *

app_name = 'basket'

urlpatterns = [
    path('api/basket/', basket, name='basket'),
    path('api/orders/', order_list, name='order-list'),
    path('api/orders/<int:order_id>/', order_detail, name='order-detail'),
    path('api/payment/', payment, name='payment'),
]
