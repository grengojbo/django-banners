from django.conf import settings


BANNER_API_URL = getattr(settings, 'BANNER_DEFAULT_API_URL', 'http://ads.sky5.com.ua/api')
BANNER_API_LOGIN = getattr(settings, 'BANNER_DEFAULT_API_LOGIN', 'username')
BANNER_API_PASSWD = getattr(settings, 'BANNER__DEFAULT_API_PASSWD', 'parol')

BANNER_SIZE_ID = getattr(settings, 'BANNER__DEFAULT_SIZE_ID', '1')
BANNER_CACHE_TIME = getattr(settings, 'BANNER__DEFAULT_CACHE_TIME', 60 * 30)
#BANNER_ = getattr(settings, 'BANNER__DEFAULT_', '')