TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ALLOWED_HOSTS = ['127.0.0.1', '<твоё_имя_пользователя>.pythonanywhere.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}