"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import logging
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(verbose=False, override=True)  # take environment variables from .env


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to file storage
MEDIA_ROOT = BASE_DIR / os.getenv("STORAGE_DIR", "data/")
STORAGE_DIR = MEDIA_ROOT

# Backend URL
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000/")
# Frontend URL
FRONT_URL = os.getenv("FRONT_URL", "http://localhost:3000")
# URL for downloading files
DOWNLOAD_URL = "storage/get/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY","django-insecure-^8b*dj4!3ull7$tm9zseji5=c1iki18zg$9(mo^k*p2@@1%p8&")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = ["*"]

#CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [FRONT_URL]
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",

    "users",
    "storage",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
#    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "back.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "back.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": os.getenv("DB_NAME", "filestorage_db"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #  {
    #    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    #  },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 6,
        },
    },
    #  {
    #    "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    #  },
    #  {
    #    "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    #  },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static", ]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("backend")

# API responses

OK_200 = {"ok": 200}
ERROR_NO_AUTH = {"error": 401, "error_msg": "Authentication needed!"}
ERROR_BAD_AUTH = {"error": 401, "error_msg": "Bad pair login/password"}
ERROR_NO_PERMIT = {"error": 401, "error_msg": "Sorry! You have no permission!"}
ERROR_BAD_PSW = {"error": 401, "error_msg": "Bad password"}
ERROR_INVALID_PSW = {"error": 401, "error_msg": "Invalid new password (too weak!)"}
ERROR_NEED_PSW = {"error": 401, "error_msg": "Password needed"}
ERROR_INVALID_LOGIN = {"error": 401, "error_msg": "Invalid login (4-20 characters a-Z,0-9, starts with letter!)"}
ERROR_NEED_LOGIN = {"error": 401, "error_msg": "Login needed"}
ERROR_EXIST_LOGIN = {"error": 400, "error_msg": "Login already exists"}
ERROR_METHOD = {"error": 405, "error_msg": "Method not allowed"}
FILE_404 = {"error": 404, "error_msg": "File not found"}
ERROR_SOME = {"error": 405, "error_msg": "Some error occurred"}
