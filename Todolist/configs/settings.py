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
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]
# https://docs.djangoproject.com/en/3.0/ref/settings/#root-urlconf
ROOT_URLCONF = 'configs.urls'

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",

    "rest_framework",

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
