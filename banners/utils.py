# -*- coding: utf-8 -*-

__author__ = 'jbo'

from django.core.cache import cache


def clear_banners_cache():
    from .models import Banner, Zone

    cache.delete("banners_zones")
    cache.delete("banners_zones_eng")

    for zone in Zone.objects.all():
        cache.delete("banner_placement:{0}".format(zone.id))

    for banner in Banner.objects.all():
        cache.delete("hbanner.{0}".format(banner.id))