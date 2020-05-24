from .common import *
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost ', 'www.pi-dal.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get("DATABASE"),
        'USER': "root",
        'PASSWORD': os.environ.get("PASSWORD"),
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
SECRET_KEY = os.environ.get("SECRET_KEY")
