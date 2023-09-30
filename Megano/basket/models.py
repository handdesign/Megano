from django.contrib.auth.models import User
from django.db import models
from catalog.models import Product


class Order(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    deliveryType = models.CharField(max_length=255)
    paymentType = models.CharField(max_length=255)
    totalCost = models.FloatField()
    status = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Basket(models.Model):
    orders = models.ManyToManyField(Order, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Basket for user {self.user.username} ({self.orders.count()} items)"
