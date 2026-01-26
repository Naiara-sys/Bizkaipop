from django.core.management.base import BaseCommand
from core.models import Category

class Command(BaseCommand):
    help = 'Poblar categorias iniciales en la base de datos'

    def handle(self, *args, **options):
        categorias = [
            {'nombre': 'Electronica', 'icono':'', 'slug':'electronica'},
            {'nombre': 'Hogar', 'icono':'', 'slug':'hogar'},
            {'nombre': 'Deportes', 'icono':'', 'slug':'deportes'},
            {'nombre': 'Moda', 'icono':'', 'slug':'moda'},
            {'nombre': 'Vehiculos', 'icono':'', 'slug':'vehiculos'},
            {'nombre': 'Libros', 'icono':'', 'slug':'libros'},
            {'nombre': 'Musica', 'icono':'', 'slug':'musica'},
            {'nombre': 'Juguetes', 'icono':'', 'slug':'juguetes'},
        ]
        
        for cat in categorias:
            obj, created = Category.objects.get_or_create(
                slug=cat['nombre'],
                defaults={
                    'nombre': cat['nombre'],
                    'icono': cat['icono']
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Categoria "{obj.nombre}" creada')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Categoria "{obj.nombre}" ya existe')
                )
            
            self.stdout.write(self.style.SUCCESS('\nProceso completado'))