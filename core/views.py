from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
#itslucyax


def home_view(request):
    productos_destacados = Product.objects.filter(is_sold=False)[:6]

    categorias_populares = [
        {'nombre': 'Electrónica', 'icono': '📱', 'slug': 'electronica'},
        {'nombre': 'Hogar', 'icono': '🏠', 'slug': 'hogar'},
        {'nombre': 'Deportes', 'icono': '⚽', 'slug': 'deportes'},
        {'nombre': 'Moda', 'icono': '👕', 'slug': 'moda'},
        {'nombre': 'Vehículos', 'icono': '🚗', 'slug': 'vehiculos'},
        {'nombre': 'Libros', 'icono': '📚', 'slug': 'libros'},
    ]

    return render(request, 'home.html', {
        'productos': productos_destacados,
        'categorias': categorias_populares,
    })




# ===== DEV 3: CATÁLOGO =====

def catalog_view(request):
    products = Product.objects.filter(is_sold=False)
    return render(request, 'catalog.html', {
        'products': products
    })


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {
        'product': product
    })


def publish_product_view(request):
    return render(request, 'publish_product.html')
