# Solución al Error 500 en Bizkaipop

## Resumen del Problema
Al integrar el trabajo de 3 desarrolladores, la aplicación generaba un **Error 500** al acceder a la página Home (`GET / HTTP/1.1 500`).

## Causa Raíz Identificada
El error principal era: **`ValueError: Missing staticfiles manifest entry for 'css/base.css'`**

Este error se producía por:
1. Configuración incorrecta de archivos estáticos en `settings.py`
2. Rutas incorrectas en los templates (`header.html` y `footer.html`)
3. Código duplicado y errores de tipeo en la configuración

## Soluciones Implementadas

### 1. Corrección de `settings.py`

#### Problemas encontrados:
- `STATIC_DIRS` (incorrecto) → debe ser `STATICFILES_DIRS`
- `STATTIC_STORAGE` (typo) → debe ser `STATICFILES_STORAGE`
- `SECURE_SSL:REDIRECT` (typo) → debe ser `SECURE_SSL_REDIRECT`
- Configuración duplicada de STATIC_URL y STATIC_ROOT
- Configuración duplicada de LOGIN/LOGOUT URLs
- `STATICFILES_STORAGE` con compresión activada en desarrollo (causa el error de manifest)

#### Solución aplicada:
```python
# Configuración correcta de archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'core' / 'static',
]

# STATICFILES_STORAGE comentado para desarrollo
# Solo se activa en producción
if 'RAILWAY_ENVIROMENT' in os.environ or 'RENDER' in os.environ:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 2. Corrección de rutas en templates

#### `header.html`
**Antes:**
```html
<img src="static/img/logo.png" alt="Bizkaipop">
```

**Después:**
```html
<img src="{% static 'img/logo.png' %}" alt="Bizkaipop">
```

#### `footer.html`
**Antes:**
```html
<!-- Bloque extra_css incorrecto -->
{% block extra_css %}
    <link rel="stylesheet" href="static/css/footer.css">
{% endblock %}

<!-- Rutas relativas incorrectas -->
<img src="../../static/img/instagram.png" alt="Instagram">
```

**Después:**
```html
<!-- Sin bloque extra_css (ya está en base.html) -->
<!-- Rutas con template tag static -->
<img src="{% static 'img/instagram.png' %}" alt="Instagram">
```

### 3. Limpieza de código duplicado

#### `bizkaipop/urls.py`
Se eliminaron importaciones y configuraciones duplicadas:
```python
# Antes: imports duplicados
from django.conf import settings #itslucyax
from django.conf.urls.static import static #itslucyax
from django.conf import settings
from django.conf.urls.static import static

# Después: imports limpios
from django.conf import settings
from django.conf.urls.static import static
```

### 4. Creación de datos de prueba

Se crearon datos de ejemplo para verificar que la aplicación funciona correctamente:
- **12 categorías** (Verduras y hortalizas, Fruta de temporada, Quesos artesanos, etc.)
- **3 productores** con coordenadas GPS para el mapa
- **6 productos** de ejemplo
- **1 usuario** de prueba (admin/admin123)

## Verificación de la Solución

✅ **Status Code 200** - La página Home carga correctamente  
✅ **Sin errores de static files** - Los archivos CSS, JS e imágenes cargan correctamente  
✅ **Templates renderizados** - Header, Footer y contenido principal se muestran  
✅ **Contexto correcto** - Las variables (productos, categorías, productores) se envían correctamente  

## Archivos Modificados

1. `bizkaipop/settings.py` - Corrección de configuración de estáticos
2. `bizkaipop/urls.py` - Eliminación de duplicados
3. `core/templates/components/header.html` - Corrección de rutas
4. `core/templates/components/footer.html` - Corrección de rutas

## Recomendaciones para el Equipo

### Para desarrollo local:
✅ El servidor ahora funciona correctamente con `python manage.py runserver`  
✅ No es necesario ejecutar `collectstatic` en desarrollo  
✅ Los archivos estáticos se sirven directamente desde `core/static/`

### Para producción:
- Ejecutar `python manage.py collectstatic` antes de desplegar
- La configuración de WhiteNoise se activará automáticamente
- STATICFILES_STORAGE con compresión se activará solo en producción

### Buenas prácticas:
1. **Siempre usar `{% static 'ruta' %}`** para referencias a archivos estáticos
2. **Nunca usar rutas relativas** como `../../static/img/logo.png`
3. **Verificar configuración** antes de integrar trabajo de múltiples devs
4. **Probar localmente** con datos de ejemplo antes de subir a producción

## Estado Final

🎉 **Error 500 RESUELTO**  
🎉 **Aplicación funcionando correctamente**  
🎉 **Integración de los 3 desarrolladores completada**

## Comandos Útiles

```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# Crear datos de prueba (ya ejecutado)
python manage.py shell < script_datos.py

# Recolectar estáticos para producción
python manage.py collectstatic

# Acceder al admin panel
# URL: http://127.0.0.1:8000/admin
# Usuario: admin
# Contraseña: admin123
```

---

**Fecha de resolución:** 2 de febrero de 2026  
**Responsable:** Dev 4 (Integración)  
**Estado:** ✅ COMPLETADO
