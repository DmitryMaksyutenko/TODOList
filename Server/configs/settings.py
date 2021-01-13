import environ

from pathlib import Path

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

env = environ.Env(DEBUG=(bool, True))

# https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key
SECRET_KEY = env("SECRET_KEY")
# https://docs.djangoproject.com/en/3.0/ref/settings/#debug
DEBUG = env("DEBUG")
# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0", "192.168.0.101"]

ROOT_URLCONF = 'configs.urls'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",

    "rest_framework",
    "corsheaders",

    "CreateList",
    "LoadList",
    "UpdateList",
    "DeleteList",
    "ExistenceList",
    "Database",
    "Api",
]

DATABASES = {
    "default": env.db(),
    "TEST": {
        "NAME": "todolist_test",
    },
}

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

SECURE_HSTS_SECONDS = 10
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = True

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://192.168.0.101:9876",
]
