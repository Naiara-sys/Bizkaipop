from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product, Category, Producer
#from django.http import HttpResponse #pruebas server

# ===== DEV 3: CAMBIOS CATÁLOGO =====
"""
#Pruebas server itslucyax
def home_view(request):
    return HttpResponse("<h1>¡Servidor OK!</h1><p>Si ves esto, tu configuración de Dev 4 es perfecta. El fallo es el HTML.</p>")
"""
def home_view(request):
    # Obtenemos los datos con nombres que el HTML entienda
    #products = Product.objects.filter(is_sold=False)[:6]
    products = Product.objects.all()[:6]
    categories = Category.objects.all()
    
    try:
        # Importante: el HTML espera 'producers' para el mapa
        producers = Producer.objects.exclude(latitude__isnull=True, longitude__isnull=True)
    except Exception:
        producers = []

    iconos = {
        'Verduras y hortalizas': '🥕', 'Fruta de temporada': '🍎', 'Quesos artesanos': '🧀',
        'Huevos de caserío': '🥚', 'Pan y harinas': '🌾', 'Mermeladas y conservas': '🍯',
        'Txakoli y sidra' : '🍾', 'Electrónica': '📱', 'Hogar': '🏠', 'Moda': '👕', 'Vehiculos' : '🚗',
    }
    #Pistas para el HTML
    categorias_list = []
    for cat in categories:
        categorias_list.append({
            'id': cat.id,
            'name': cat.name,
            'icono': iconos.get(cat.name, '🛒')
        })
    
    context = {
        'productos': products,    # Lo que espera el HTML ahora mismo
        'products': products,     # Por si el HTML cambia
        'productos_destacados': products,      # Nombre view anterior
        'categorias': categorias_list, 
        'producers': producers,
    }
    """
    context = {
        'productos': products,    # Por si acaso usa 'productos'
        'products': products,     # Por si el HTML usa 'products'
        'categorias': categories, # Por si el HTML usa 'categorias'
        'categories': categories, # Por si el HTML usa 'categories'
        'producers': producers,   # La que usa el mapa
    }
    """
    return render(request, 'home.html', context)

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


# ===== AUTENTICACIÓN =====

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    
    return render(request, 'login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Las contraseñas no coinciden'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'El nombre de usuario ya existe'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'El email ya está registrado'})
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('home')
    
    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('home')
