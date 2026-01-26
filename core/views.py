from django.shortcuts import render, get_object_or_404
from .models import Product, Category




from .models import Product, Category

def home_view(request):
    productos_destacados = Product.objects.filter(is_sold=False)[:6]
    categorias = Category.objects.all()

    iconos = {
        'Electrónica': '📱',
        'Hogar': '🏠',
        'Deportes': '⚽',
        'Moda': '👕',
        'Vehículos': '🚗',
        'Alimentación': '🍎',
    }

    categorias_populares = []
    for categoria in categorias:
        categorias_populares.append({
            'id': categoria.id,
            'nombre': categoria.name,
            'icono': iconos.get(categoria.name, '🛒'),
        })

    return render(request, 'home.html', {
        'productos': productos_destacados,
        'categorias': categorias_populares,
    })





# ===== DEV 3: CATÁLOGO =====

def catalog_view(request):
    products = Product.objects.filter(is_sold=False)

    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'catalog.html', {
        'products': products,
        'categories': categories,
    })


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {
        'product': product
    })


def publish_product_view(request):
    return render(request, 'publish_product.html')
