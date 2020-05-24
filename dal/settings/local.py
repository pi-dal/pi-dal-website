from .common import *
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'pi-dal.db'),
    }
}
SECRET_KEY = '__8)+a)-nc_fwmz948eyv&n7l2uw-r70bb8q%@m_4f=y^9#der'

