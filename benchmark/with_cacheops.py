from settings import *

INSTALLED_APPS = INSTALLED_APPS + ('cacheops',)

CACHEOPS_REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 10,
}

CACHEOPS_DEFAULTS = {
    'timeout': 60*60
}

CACHEOPS = {
    '*.*': {},
}
