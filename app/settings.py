INSTALLED_APPS = [
    # ... other apps
    'books',
    'authors',
    'genres',
    'users',
    'orders',
    'reviews',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore_db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

