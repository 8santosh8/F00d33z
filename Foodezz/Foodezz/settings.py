"""
Django settings for Foodezz project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#u9wm_bw6th9##b+ix@v=u#a(97z#kg3&l9a@ut$t8@3f65@@s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'Hotel.apps.HotelConfig',
    'Users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'materialize',
    'widget_tweaks',
    'blog',
    'payments',
    'gpstrack',
    'paypal.standard.ipn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Foodezz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <- Here
                'social_django.context_processors.login_redirect', # <- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'Foodezz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
     # 'default': {
     #     'ENGINE': 'django.db.backends.sqlite3',
     #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     # }
    'default': {
       'ENGINE': 'mysql.connector.django',
       'NAME': 'Foodezz',
       # 'USER': os.environ.get('root'),
       # 'PASSWORD': os.environ.get('root'),
       'USER': os.environ.get('MySQLUser'),
       'PASSWORD': os.environ.get('MySQLPass'),
       'HOST': '127.0.0.1',
       'PORT': '3306',
    }

       # 'HOST': '127.0.0.1',
       # 'PORT': '3306',
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# ============================= Basic directory locations ===========================

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
    ]

MEDIA_ROOT = os.path.join(BASE_DIR,'Media')
MEDIA_URL = '/Media/'

# ===================== Specifications for the installed package properties =======================

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# ===================== Basic url redirects definations ====================

LOGIN_REDIRECT_URL = 'Users-Home'
LOGOUT_REDIRECT_URL = 'Users-Home'
LOGIN_URL = 'Users-Login'


# ===================== basic information for the email to connect through net ==================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'hemanthtemp07@gmail.com'
EMAIL_HOST_PASSWORD = 'UchihaMadara'


# ===================== Programs through which one can login to the system ======================

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication

    'django.contrib.auth.backends.ModelBackend',
)

# ==================== Client key and secret keys for the same =========================

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '420290905831-scnnu0ebj6j82e37ok5dt43kbnqor3tv.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Io7CqjTtzQbldkCZn-kKVSDX'
