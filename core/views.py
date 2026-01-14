from django.shortcuts import render

# Create your views here.
#itslucyax
from django.shortcuts import render

def home_view(request):
    productos_destacados = [
        {
            'id': 1,
            'titulo': 'Bicicleta de montaña',
            'precio': 250.00,
            'ubicacion': 'Bilbao',
            'imagen': 'https://via.placeholder.com/300x200?text=Bicicleta'
        },
        {
            'id': 2,
            'titulo': 'iPhone 12 Pro',
            'precio': 450.00,
            'ubicacion': 'Getxo',
            'imagen': 'https://via.placeholder.com/300x200?text=iPhone'
        },
        {
            'id': 3,
            'titulo': 'Mesa de comedor',
            'precio': 120.00,
            'ubicacion': 'Barakaldo',
            'imagen': 'https://via.placeholder.com/300x200?text=Mesa'
        },
        {
            'id': 4,
            'titulo': 'PlayStation 5',
            'precio': 380.00,
            'ubicacion': 'Bilbao',
            'imagen': 'https://via.placeholder.com/300x200?text=PS5'
        },
        {
            'id': 5,
            'titulo': 'Guitarra eléctrica',
            'precio': 200.00,
            'ubicacion': 'Durango',
            'imagen': 'https://via.placeholder.com/300x200?text=Guitarra'
        },
        {
            'id': 6,
            'titulo': 'Cafetera Nespresso',
            'precio': 60.00,
            'ubicacion': 'Bilbao',
            'imagen': 'https://via.placeholder.com/300x200?text=Cafetera'
        },
    ]
    #CAMBIAR ICONOS
    categorias_populares = [
        {'nombre': 'Electrónica', 'icono': '📱', 'slug': 'electronica'},
        {'nombre': 'Hogar', 'icono': '🏠', 'slug': 'hogar'},
        {'nombre': 'Deportes', 'icono': '⚽', 'slug': 'deportes'},
        {'nombre': 'Moda', 'icono': '👕', 'slug': 'moda'},
        {'nombre': 'Vehículos', 'icono': '🚗', 'slug': 'vehiculos'},
        {'nombre': 'Libros', 'icono': '📚', 'slug': 'libros'},
    ]
    
    context = {
        'productos': productos_destacados,
        'categorias': categorias_populares,
    }
    
    return render(request, 'home.html', context)