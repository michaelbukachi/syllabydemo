from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    file = models.ImageField()
