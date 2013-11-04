from django.conf import settings


BANNER_API_URL = getattr(settings, 'BANNER_DEFAULT_API_URL', 'http://ads.sky5.com.ua/api')
BANNER_API_LOGIN = getattr(settings, 'BANNER_DEFAULT_API_LOGIN', 'username')
BANNER_API_PASSWD = getattr(settings, 'BANNER_DEFAULT_API_PASSWD', 'parol')

BANNER_SIZE_ID = getattr(settings, 'BANNER_DEFAULT_SIZE_ID', '1')
BANNER_CACHE_TIME = getattr(settings, 'BANNER_DEFAULT_CACHE_TIME', 60 * 30)
BANNER_CACHE_TIME_VIEW = getattr(settings, 'BANNER_DEFAULT_CACHE_TIME_VIEW', 60 * 10)
BANNER_URL = getattr(settings, 'BANNER_DEFAULT_URL', 'localhost')
BANNER_IP = getattr(settings, 'BANNER_DEFAULT_IP', '127.0.0.1:8000')
BANNER_IMG = getattr(settings, 'BANNER_DEFAULT_TPL_IMG', "<a href='{go}' target='{target}' style='border-width:0;'><img src='{src}' width='{width}' height='{height}' style='border-width:0'/></a>")
#BANNER_ = getattr(settings, 'BANNER__DEFAULT_', '')




