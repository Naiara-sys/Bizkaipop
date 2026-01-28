






from django.contrib import admin
from .models import Category, Product, ProductImage, Producer

admin.site.register(Category)
admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(ProductImage)

