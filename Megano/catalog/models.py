from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Specification(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


def product_image_directory_path(instance: 'Product', filename: str) -> str:
    return f'products/product_{instance.pk}/preview/{filename}'


class Product(models.Model):
    category = models.IntegerField()
    title = models.CharField(max_length=255)
    price = models.FloatField()
    salePrice = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    freeDelivery = models.BooleanField()
    images = models.ImageField(null=True, blank=True, upload_to=product_image_directory_path)
    tags = models.ManyToManyField(Tag, blank=True)
    reviews = models.ManyToManyField('Review', blank=True, related_name='products')
    specifications = models.ManyToManyField(Specification, blank=True)
    rating = models.FloatField(null=True, blank=True)
    is_banner_product = models.BooleanField(default=False)

    def __str__(self):
        return f'Product(pk={self.pk}, title={self.title!r})'


class Review(models.Model):
    author = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews_for_product')

    def __str__(self):
        return f"Review by {self.author}"
