from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Producer


# ===== DEV 3: CAMBIOS CATÁLOGO =====
def home_view(request):
    productos_destacados = Product.objects.filter(is_sold=False)[:6]
    categorias = Category.objects.all()

    producers = Producer.objects.exclude(
        latitude__isnull=True,
        longitude__isnull=True
    )

    iconos = {
        'Verduras y hortalizas': '🥕',
        'Fruta de temporada': '🍎',
        'Quesos artesanos': '🧀',
        'Huevos de caserío': '🥚',
        'Pan y harinas': '🌾',
        'Mermeladas y conservas': '🍯',
        'Txakoli y sidra': '🍾',
        'Electrónica': '📱',
        'Hogar': '🏠',
        'Moda': '👕',
        'Vehículos': '🚗',
    }

    ORDEN_CATEGORIAS = [
        'Verduras y hortalizas',
        'Fruta de temporada',
        'Quesos artesanos',
        'Huevos de caserío',
        'Pan y harinas',
        'Mermeladas y conservas',
        'Txakoli y sidra',
        'Electrónica',
        'Hogar',
        'Moda',
        'Vehículos',
    ]

    categorias_dict = {c.name: c for c in categorias}

    categorias_ordenadas = []
    for nombre in ORDEN_CATEGORIAS:
        if nombre in categorias_dict:
            categoria = categorias_dict[nombre]
            categorias_ordenadas.append({
                'id': categoria.id,
                'name': categoria.name,
                'icono': iconos.get(categoria.name, '🛒'),
            })

    return render(request, 'home.html', {
        'productos': productos_destacados,
        'categorias': categorias_ordenadas,
        'producers': producers,
    })

# ===== DEV 2: CONTACTO =====

def contacto_view(request):
    return render(request,'components/contacto.html') 


# ===== DEV 3: CATÁLOGO =====

def catalog_view(request):
    products = Product.objects.filter(is_sold=False)
    categories = Category.objects.all()

    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

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
