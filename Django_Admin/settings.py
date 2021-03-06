"""
Django settings for Django_Admin project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from Django_Admin.user_settings import Database_Name, Host_Name, Static_Path, Email_Sender, Redis_Data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c6g1#fj#c6urfp(pk5n!9ec#@mcj_b#mo-wkcg3d!7l%&k6sw#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Applications.Global',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django_Admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Django_Admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



#????????????
if DEBUG == True:
    SITE_URL = 'http://127.0.0.1:8000/'
else:
    SITE_URL = Host_Name

STATIC_URL = '/static/'
# ??????????????????
STATIC_ROOT = Static_Path

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

if DEBUG == True:
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
else:
    MEDIA_ROOT = os.path.join(SITE_URL, 'uploads')

MEDIA_URL = '/media/'

X_FRAME_OPTIONS = 'SAMEORIGIN'

# ????????????
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False   #????????????TLS??????????????????(???????????????????????????????????????????????????????????????????????????)
EMAIL_USE_SSL = False    #????????????SSL?????????qq????????????????????????
EMAIL_HOST = 'smtp.163.com'   #????????????????????? ??? SMTP????????????????????????163??????
EMAIL_PORT = 25     #????????????SMTP???????????????
EMAIL_HOST_USER = 'louisyoung163@163.com'    #???????????????????????????
EMAIL_HOST_PASSWORD = 'GUTCEBDOYWMHGLWY'         #???????????????????????????(???????????????????????????)
EMAIL_FROM = Email_Sender + '<louisyoung163@163.com>'

# django-redis ????????????
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://45.40.234.190:6379/" + Redis_Data,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# redis ?????? session backend ??????
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"


# ??????????????????
TINYMCE_DEFAUT_CONFIG = {
    'theme':'advanced',
    'width':600,
    'height':400,
}

# ??????Django??????????????????
DEFAULT_FILE_STORAGE = 'utils.fdfs.storage.FastDFS_Storage'

# ??????FastDFS?????????client.config??????
FDFS_CLIENT_CONF = './utils/fdfs/client.conf'

# FastDFS??????
FDFS_URL = 'http://45.40.234.190:8888/'
