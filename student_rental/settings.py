import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Keep development convenient while allowing PythonAnywhere to provide its
# production secret through an environment variable.
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-local-development-only',
)
DEBUG = os.environ.get('DJANGO_DEBUG', 'true').lower() in {'1', 'true', 'yes'}
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        'DJANGO_ALLOWED_HOSTS',
        'localhost,127.0.0.1',
    ).split(',')
    if host.strip()
]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','accounts','listings','interactions']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='student_rental.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='student_rental.wsgi.application'
ASGI_APPLICATION='student_rental.asgi.application'
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
AUTH_USER_MODEL='accounts.User'
AUTH_PASSWORD_VALIDATORS=[{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'}]
LANGUAGE_CODE='en-us'
TIME_ZONE='Asia/Kolkata'
USE_I18N=True
USE_TZ=True
STATIC_URL='static/'
STATICFILES_DIRS=[BASE_DIR/'static']
STATIC_ROOT=BASE_DIR/'staticfiles'
MEDIA_URL='media/'
MEDIA_ROOT=BASE_DIR/'media'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
LOGIN_URL='accounts:login'
LOGIN_REDIRECT_URL='listings:home'
LOGOUT_REDIRECT_URL='listings:home'
