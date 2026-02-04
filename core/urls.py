
# itslucyax
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    # ===== DEV 3: CATÁLOGO =====
    path('catalog/', views.catalog_view, name='catalog'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('publish/', views.publish_product_view, name='publish_product'),
    path('contacto/', views.contacto_view, name='contacto'),

    # ===== AUTENTICACIÓN =====
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
