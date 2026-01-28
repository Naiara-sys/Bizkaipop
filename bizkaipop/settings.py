"""
Django settings for bizkaipop project.

RESPONSABLE : DEV 4
"""
# ==============================================================================
# AVISO PARA EL EQUIPO
# ==============================================================================
# Este archivo es gestionado por el Dev 4(lucia) para asegurar el despliegue en Railway.
# 1. Si necesitas añadir una APP nueva, añádela en INSTALLED_APPS abajo.
# 2. Si el servidor no te arranca, revisa tu archivo .env antes de tocar aquí.
# 3. Para cualquier otro cambio (Middlewares, Databases, etc.), AVISADME.
# ==============================================================================

from pathlib import Path
from decouple import config
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-)4bx*itix@2)ne369v-(86dzq)7f*-m(hlcj0*f9+gaapwnxlv')
#SECURIDAD AVISO: no correr con debug activado en produccion
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='django-insecure-)4bx*itix@2)ne369v-(86dzq)7f*-m(hlcj0*f9+gaapwnxlv').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core' #itslucyax
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bizkaipop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'], #itslucyax
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bizkaipop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config (
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3'),
        conn_max_age=600 #tiempo validz en segundos
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# Si añades carpetas de static en core/static Django las encontrara
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_DIRS = [
    BASE_DIR / 'core' / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIR = [
    BASE_DIR / 'core' / 'static',
]

# Rutas de autenticación (Gestionadas por Dev 1- AIMAR)
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'register'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Media files (Imágenes subidas por usuarios para productos/perfil)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ==============================================================================
# CONFIGURACIÓN AVANZADA DE DEPLOYMENT (No tocar sin avisar al Dev 4)
# ==============================================================================

#Optimizacion archivos estaticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

if 'RAILWAY_ENVIROMENT' in os.environ or 'RENDER' in os.environ:
    #Dominios permitidos en la nube
    ALLOWED_HOSTS.append('.railway.app')
    ALLOWED_HOSTS.append('.onrender.com')
    
    if 'DATABASES_URL' in os.environ:
        DATABASES['default'] = dj_database_url.config(
            conn_max_age=600,
            con_health_checks=True
        )
        
    #Seguridad forzada en produccion
    DEBUG = False
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True