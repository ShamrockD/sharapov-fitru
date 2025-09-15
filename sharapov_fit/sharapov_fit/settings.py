from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-u#_y79sn*q8_0z-0u=+u+ntsdaj!-4ystjr--0q@%eohzw0)^g'
SECRET_KEY = os.environ.get('SECRET_KEY', 'super_secret_key_for_my_django_project')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '0').lower() in ['1', 'true', 'yes']
print(f"ДЕБАГ СЕЙЧАС В СОСТОЯНИИ: {DEBUG}")
# DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
else:
    allowed_hosts = os.environ.get('DJANGO_ALLOWED_HOSTS', '')
    # ALLOWED_HOSTS = allowed_hosts.split(',') if allowed_hosts else []
    ALLOWED_HOSTS = ['citylag.ru', 'www.citylag.ru', 'localhost', '127.0.0.1', 'web', 'django']

CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "core",
    "promo",
    "courses",
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

ROOT_URLCONF = 'sharapov_fit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sharapov_fit.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

if not all([DATABASES['default']['NAME'], DATABASES['default']['USER'], DATABASES['default']['HOST']]):
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }


# Password validation

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Для разработки
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# Для правильного определения IP
# IPWARE_META_PRECEDENCE_ORDER = (
#     'HTTP_X_FORWARDED_FOR', 
#     'X_FORWARDED_FOR', 
#     'HTTP_CLIENT_IP',
#     'HTTP_X_REAL_IP',
#     'HTTP_X_FORWARDED',
#     'HTTP_X_CLUSTER_CLIENT_IP',
#     'HTTP_FORWARDED_FOR',
#     'HTTP_FORWARDED',
#     'HTTP_VIA',
#     'REMOTE_ADDR'
# )

# Условно применяем HTTPS настройки только в production
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    # SECURE_BROWSER_XSS_FILTER = True
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = False
    # SECURE_SSL_REDIRECT = True
    USE_X_FORWARDED_HOST = True
    USE_X_FORWARDED_PORT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    # Для разработки отключаем HTTPS-related настройки
    USE_X_FORWARDED_HOST = False
    SECURE_PROXY_SSL_HEADER = None
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'