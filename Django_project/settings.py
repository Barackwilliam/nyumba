
import os
import cloudinary
import cloudinary_storage
from pathlib import Path
import django_heroku
import dj_database_url
from dotenv import load_dotenv
import dotenv
import cloudinary.api
from decouple import config



load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


dotenv_file = os.path.join(BASE_DIR, ".env") 
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pvcPAFrkq9V6lgl_AIryxut9DrMRFA5b0L2gmmU_Ic5NCgf7Lk3Cqbp3xdvYyZhyLs8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.humanize',
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',

    'Myapp',
    'chat',
    'channels',
    'Blog',
    'django_filters',
    'storages',
    'social_django',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Django_project.middleware.MethodNotAllowedMiddleware',
    'Django_project.middleware.BlockScrapersMiddleware',  # Ongeza hapa

    
]

ROOT_URLCONF = 'Django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Django_project.wsgi.application'

#ASGI application
ASGI_APPLICATION = 'Django_project.asgi.application'
CHANNEL_LAYERS = {

        "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }

}


# supabase database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres', 
        'USER': 'postgres.pwztkimkloomauuuzvhx',  
        'PASSWORD': 'NyumbaChap', 
        'HOST': 'aws-0-us-west-1.pooler.supabase.com',  
        'PORT': '5432',  
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }





# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Dar_es_Salaam'
USE_TZ = True
USE_I18N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    BASE_DIR / "static", ]

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

STATIC_ROOT = BASE_DIR / "staticfiles"  

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Cloudinary settings

cloudinary.config(
    cloud_name='drc3xiipg',  # Your Cloudinary cloud name
    api_key='321181265585861',   # Replace with your Cloudinary API key
    api_secret='KA2L_qJUCyBBZFcyeQDGzH1kfUo',  # Replace with your Cloudinary API secret
)




CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'drc3xiipg',  # Jina lako la Cloudinary
    'API_KEY': '321181265585861',  # API key yako
    'API_SECRET': 'KA2L_qJUCyBBZFcyeQDGzH1kfUo'  # API secret yako
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = 'https://res.cloudinary.com/drc3xiipg/'


#language changer
USE_I18N = True
USE_L10N = True
USE_TZ = True
#language support
LANGUAGES = [
    ('en','English'),
    ('sw','Swahili'),
]

#path for translation files
LOCALE_PATHS=[
    os.path.join(BASE_DIR,'locale'),
]
#Default language
LANGUAGE_CODE = 'en'

JAZZMIN_SETTINGS = {
    'site_header':" NyumbaChap",
    #'site_logo':" assets/images/bg1.png",
     'site_brand': "NyumbaChap.com",
    #'site_logo':" assets/images/4.png",
    'copyright':" NyumbaChap.com",
}


DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

django_heroku.settings(locals())



LOGIN_URL = '/login/'




# email configurationss

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.zoho.com"  # SMTP server ya Zoho
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "info@nyumbachap.online"  # Badilisha na email yako ya Zoho
EMAIL_HOST_PASSWORD = "Chipindi@123"  # Badilisha na password yako ya Zoho
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



# RECAPTCHA_PUBLIC_KEY = '6LfuUAQrAAAAAIopNWeR-dfvr9-9MVE9IMoDG5BL'
# RECAPTCHA_PRIVATE_KEY = '6LfuUAQrAAAAALQ8np7CXxpyFOMzIOTKdiUgjbKi'


# client_id: 27751749322-khts80a7a7bf7qdhr31aqlfticr7mraj.apps.googleusercontent.com
# client_secret: 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

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'  # au page yoyote baada ya login
LOGOUT_REDIRECT_URL = 'popular_featured'



# Social Auth Settings
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)





# from pyuploadcare.dj import get_fields

UPLOADCARE = {
    "pub_key": "b554dba7565f88537168",
    "secret": "86092ed986a8b1788d3c",
}


# Session Settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True




SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '27751749322-khts80a7a7bf7qdhr31aqlfticr7mraj.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['picture', 'email']


RECAPTCHA_PUBLIC_KEY = '6Lfr4xUrAAAAACmeCbB_ii2950eZIQBfWUfOX0Kc'
RECAPTCHA_PRIVATE_KEY = '6Lfr4xUrAAAAAHJxI7wm4xFza7BTBYotysJocKbn'