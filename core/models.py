from django.db import models
from django.conf import settings

# ===== DEV 3: PRODUCTOS =====

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=150)
    municipality = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_ecological = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} · {self.municipality}"


class Product(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products'
    )

    producer = models.ForeignKey(
        Producer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )
    location = models.CharField(max_length=100)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='products/')





