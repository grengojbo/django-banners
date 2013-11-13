# -*- coding: utf-8 -*-

__author__ = 'jbo'

from django.core.cache import cache
import datetime as dt

def clear_banners_cache():
    from .models import Banner, Zone

    cache.delete("banners_zones")
    cache.delete("banners_zones_eng")

    for zone in Zone.objects.all():
        cache.delete("banner_placement:{0}".format(zone.id))

    for banner in Banner.objects.all():
        cache.delete("hbanner.{0}".format(banner.id))


def get_expires():
    # Сколько секунд в 1 дне
    sec_in_day = 86400
    # dt.datetime.today().weekday()
    d = dt.datetime.today()
    t = sec_in_day - (60 * 60 * d.hour) - (60 * d.minute)
    if t > 10:
        return t
    else:
        return sec_in_day