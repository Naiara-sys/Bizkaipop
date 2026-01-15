
# itslucyax
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    # ===== DEV 3: CATÁLOGO =====
    path('catalog/', views.catalog_view, name='catalog'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('publish/', views.publish_product_view, name='publish_product'),
]
