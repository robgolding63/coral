import os

PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Rob Golding', 'rob@robgolding.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'coral'             # Or path to database file if using sqlite3.
DATABASE_USER = 'coral'             # Not used with sqlite3.
DATABASE_PASSWORD = 'f75amc0x'         # Not used with sqlite3.
DATABASE_HOST = 'mysql'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://projects.robgolding.com/media/coral/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't636b^58v@jo2qi#)t3#u%oshb+zv0_m!+6ff1pgpotqjxcojj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'coral.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PATH, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	'django.core.context_processors.request',
	'coral.tracker.context_processors.filter',
)

AUTH_PROFILE_MODULE = 'users.Profile'

ABSOLUTE_URL_OVERRIDES = {
	'auth.user': lambda o: "/coral/users/%s/" % o.username,
}

LOGIN_URL = '/coral/accounts/login/'

LOGIN_REDIRECT_URL = '/coral/'

FORCE_LOWERCASE_TAGS = True

MAX_TAG_LENGTH = 20

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'profiles',
    'tagging',
    'haystack',
    'coral.accounts',
    'coral.tracker',
    'coral.users',
    'coral.search',
    'coral.svn_revision',
)

HAYSTACK_SITECONF = 'coral.search_sites'

HAYSTACK_SEARCH_ENGINE = 'whoosh'

HAYSTACK_WHOOSH_PATH = '/home/whoosh/coral_index'

try:
	from local_settings import *
except ImportError:
	pass
