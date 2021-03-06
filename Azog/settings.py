"""
Django settings for Azog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wbp9#x=oa)8ioxh668kk+pe2fhg-=$w8^wbtrq*$a&^7^mp7c@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'takeaway',
	'south',
 'notifications',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Azog.urls'

WSGI_APPLICATION = 'Azog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


import os
is_local = False
try:
	is_local = os.environ['local']
except KeyError:
	print "Environment is not local"

DATABASES = {
    	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    	}
}


if not is_local:
	import dj_database_url
	DATABASES['default'] =  dj_database_url.config()



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'



# LOGIN Pge STuff

LOGIN_URL = '/login/'

LOGOUT_URL = '/static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = '/static/'


#Template Location
TEMPLATE_DIRS =(
                os.path.join(os.path.dirname(os.path.dirname(__file__)),"static","templates")
                )


if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)),"static","static")
    MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)),"static","media")
    STATICFILE_DIRS = os.path.join(os.path.dirname(os.path.dirname(__file__)),"static","static")
