# -*- coding: utf-8 -*-
import random
from datetime import datetime as dt
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from django.db.models import Q, F
from .models import Zone, Placement, Banner, BannerSize, BannerShow, BannerClick
from django.core.urlresolvers import reverse
from django.core.cache import cache
from . import app_settings as bset
#try:
#    from hashlib import md5
#except ImportError:
#    from md5 import md5
#from time import time

import logging

logger = logging.getLogger(__name__)


def placement(request, placement_id, zone_id):
    p = get_object_or_404(Placement, id=placement_id)
    p.clicks += 1
    p.save()
    return HttpResponseRedirect(p.banner.foreign_url)


def clicks(request, banner_id, zone_id, ses):
    user_key = None
    clien_type = None
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']
    if request.session.session_key:
        logger.debug(u'request session: {0}'.format(request.session.session_key))
        user_key = request.session.session_key
    if ses == 'no':
        audits = 2
    else:
        audits = 1
    cur_banner = cache.get("banner:show:{0}:{1}:{2}".format(banner_id, zone_id, user_key))
    b = get_object_or_404(Banner, id=banner_id, is_active=True)
    if not cur_banner:
        s = BannerShow.objects.filter(banner_id=2, zone_id=1)
        cache.set("banner:show:{0}:{1}:{2}".format(banner_id, zone_id, user_key), s[0], bset.BANNER_CACHE_TIME_VIEW)
    click_banner = cache.get("banner:click:{0}:{1}:{2}".format(banner_id, zone_id, user_key))
    if not click_banner:
        if clien_type == 'mac':
            res = BannerClick.objects.filter(banner_id=banner_id, zone_id=zone_id,
                                             user_mac=user_key).update(shows=F('clicks') + 1)
        else:
            res = BannerClick.objects.filter(banner_id=banner_id, zone_id=zone_id,
                                             ses=user_key).update(shows=F('clicks') + 1)
        if res.count() > 0:
            s = res
        else:
            s = b.click(request, zone_id, audits)
        click_banner = b.foreign_url
        cache.set("banner:click:{0}:{1}:{2}".format(banner_id, zone_id, user_key), click_banner, bset.BANNER_CACHE_TIME_VIEW)
        logger.debug('click: {0}'.format(s))
    logger.debug(u'HttpResponseRedirect: {0}'.format(click_banner))
    try:
        return HttpResponseRedirect(click_banner)
    except Exception:
        logger.error('No HttpResponseRedirect banner_id: {0}, zone_id: {1}'.format(banner_id, zone_id))


def shows(request, banner_id, zone_id, ses, user_mac=None):
    #src_url = cache.get("hbanner:{0}:src:{1}".format(banner_id, zone_id))
    user_key = None
    clien_type = None
    btype = None
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']
    if request.session.session_key:
        logger.debug(u'request session: {0}'.format(request.session.session_key))
        user_key = request.session.session_key
        btype = request.session['banner_type']
    if ses == 'no':
        audits = 2
    else:
        audits = 1
    cur_banner = cache.get("banner:show:{0}:{1}:{2}".format(banner_id, zone_id, user_key))
    src_url = cache.get("hbanner:{0}:{1}".format(banner_id, btype))
    b = get_object_or_404(Banner, id=banner_id, is_active=True)

    if not src_url:
        src_url = u'{0}{1}'.format(bset.BANNER_URL, reverse('banners:shows',
                                                            kwargs={'banner_id': b.id, 'zone_id': zone_id, 'ses': ses}))
    if not cur_banner:
        if clien_type == 'mac':
            res = BannerShow.objects.filter(banner_id=banner_id, zone_id=zone_id,
                                            user_mac=user_key).update(shows=F('shows') + 1)
        else:
            res = BannerShow.objects.filter(banner_id=banner_id, zone_id=zone_id,
                                            ses=user_key).update(shows=F('shows') + 1)
        if res.count() > 0:
            s = res
        else:
            # зачисляем только уникальные просмотры
            s = b.show(request, zone_id, audits)
        cache.set("banner:show:{0}:{1}:{2}".format(banner_id, zone_id, user_key), s, bset.BANNER_CACHE_TIME_VIEW)
        logger.debug('show: {0}'.format(s))
    #p = get_object_or_404(Placement, id=zone_id)
    #p.clicks += 1
    #p.save()
    #logger.debug(u'request: {0}'.format(request))
    logger.debug(u'HttpResponseRedirect: {0}'.format(src_url))
    return HttpResponseRedirect(src_url)


def code(request, zone_id, btype='name'):
    '''http://ads.sky5.com.ua/openx/www/delivery/spc.php?
    zones=wifi-ad%3D15%7C&nz=1&source=&r=14698272&charset=UTF-8
    &loc=http%3A//localhost%3A9000/
    http://127.0.0.1:8000/b/code/1/ip/
    '''
    vquery = ''
    vses = 'no/'
    if 'loc' in request.GET:
        logger.debug('loc: {0}'.format(request.GET['loc']))
        #vquery += 'loc={0}&'.format(request.GET['loc'])
    if 'charset' in request.GET:
        logger.debug('charset: {0}'.format(request.GET['charset']))
    if 'r' in request.GET:
        logger.debug('r: {0}'.format(request.GET['r']))
    if 'source' in request.GET:
        logger.debug('source: {0}'.format(request.GET['source']))
    if 'nz' in request.GET:
        logger.debug('nz: {0}'.format(request.GET['nz']))
    #if 'loc' in request.GET:
    #    logger.debug('loc: {0}'.format(request.GET['loc']))
    if vquery.__len__() > 3:
        vquery += 'v=1'
    #cache.get()
    request.session['last_activity'] = dt.now()
    if request.session.session_key:
        logger.debug(u'CODE request session: {0}'.format(request.session.session_key))
        user_key = request.session.session_key
        vses = '{0}/'.format(request.session.session_key)
    if request.GET:
        logger.debug("request.GET.urlencode: {0}".format(request.GET.urlencode))
        vquery += "?{0}".format(request.META['QUERY_STRING'])
    res = gen_banner_code(request, zone_id, var=False)
    if btype == 'ip':
        go = bset.BANNER_IP
    else:
        go = bset.BANNER_URL
    #return HttpResponse(template.render(context), mimetype="application/x-javascript")
    logger.debug("[code] request.META: {0}".format(request.META))
    return HttpResponse(res.format('http://', go, vses, vquery), mimetype="application/x-javascript")


def zones(request, zone_id):
    template = get_template("banners/zones.html")
    zone = Zone.objects.get(id=zone_id)
    context = Context({
        "banner_code": gen_banner_code(request, zone_id),
        "MEDIA_URL": bset.settings.MEDIA_URL,
        "html_after_banner": zone.html_after_banner,
        "html_pre_banner": zone.html_pre_banner
    })
    return HttpResponse(template.render(context))


def w_choice(lst):
    n = random.uniform(0, 1)
    for item, weight, plc in lst:
        if n < weight:
            break
        n = n - weight
    return item, plc


def normalize(lst):
    sum, new_lst = 0., []
    for item, weight, plc in lst:
        sum += weight
    for item, weight, plc in lst:
        new_lst.append([item, weight/sum, plc])
    return new_lst


def gen_code(b, plc, zone, request, go=None, zone_el='wifi-ad'):
    code = u""
    logger.debug("Zone type: {0}".format(zone))
    img_url = cache.get("hbanner:{0}:g".format(b.id))
    if not img_url:
        img_url = b.img_file.url if b.img_file else ""
        cache.set("hbanner:{0}:g".format(b.id), img_url, bset.BANNER_CACHE_TIME)
    swf_url = cache.get("hbanner:swf:{0}".format(b.id))
    if not swf_url:
        swf_url = b.swf_file.url if b.swf_file else ""
        cache.set("hbanner:f:{0}".format(b.id), swf_url, bset.BANNER_CACHE_TIME)
    logger.debug("img: {1} url: {0}".format(img_url, b.img_file))
    if b.banner_type == 'f':
        # Flash-баннер
        banner_href = reverse("banners:placement", kwargs={"placement_id": plc["id"]})
        template = get_template("banners/gen_banner_code.html")
        context = Context({
            "banner_width": b.width,
            "banner_height": b.height,
            "data": u"{0}?banner_href={1}".format(swf_url, banner_href),
            "swf_url": swf_url,
            "banner_href": banner_href,
            "img_url": img_url,
            "foreign_url": b.foreign_url,
        })
        code += template.render(context)
    # графические баннеры
    elif b.banner_type == 'g':
        if b.foreign_url:
            src_url = cache.get("hbanner:{0}:src:{1}".format(b.id, zone["id"]))
            if not src_url:
                src_url = reverse('banners:show', kwargs={'banner_id': b.id, 'zone_id': zone["id"]})
                cache.set("hbanner:{0}:src:{1}".format(b.id, zone["id"]), src_url, bset.BANNER_CACHE_TIME)
            code = bset.BANNER_IMG.format(go=reverse("banners:clicks",
                                                     kwargs={"banner_id": b.id, 'zone_id': zone["id"]}),
                                          src=src_url, width=b.width, height=b.height, target=b.url_target)
    # html баннеры
    elif b.banner_type == 'h':
        code = b.html_text
        src_url = ''
    if int(zone['code_view']) == 2:
        # показывать баннер для WiFi Cisco
        code = reverse("banners:clicks", kwargs={"banner_id": b.id, 'zone_id': zone["id"]})
        template = get_template("banners/zones.js")
        context = Context({
            'banner_href': code,
            "banner_width": b.width,
            "banner_height": b.height,
            'go': go,
            'zone_el': zone_el,
            "banner_code": src_url,
            "MEDIA_URL": bset.settings.MEDIA_URL,
            "html_after_banner": zone["html_after_banner"],
            "html_pre_banner": zone["html_pre_banner"]
        })
        return template.render(context)
    else:
        return u"{0}{1}{2}".format(zone["html_pre_banner"], code, zone["html_after_banner"])


def gen_banner_code(request, zone_id, var=False):
    pr = {1: 3, 2: 5, 3: 7, 4: 9, 5: 11, 6: 13, 7: 15, 8: 17, 9: 20}  # Распределение вероятностей
    probabilities = []
    hbanner = u""
    #site = Site.objects.get_current()
    #banner_site_url = getattr(settings, 'BANNER_SITE_URL', 'http://%s/' % site.domain)
    if 'banners.clients' in request.META:
        request.META['banners.clients'] = []

    # TODO: разобратся с зонами кеширование, проверка
    #zones = getattr(request, "banners_zones", None)
    #zones_eng = getattr(request, "banners_zones_eng", None)
    zones = None
    zones_eng = None
    # Поиск зоны
    zone_id = str(zones_eng[zone_id]) if (zones and zone_id in zones_eng) else str(zone_id)

    # Поиск по переменным
    if not var:
        var = request.GET.get('var', False)
    varnot = request.GET.get('varnot', False)

    try:
        if zone_id.isdigit():
            if zones and int(zone_id) in zones:
                zone = zones[int(zone_id)]
                logger.debug("ZONE zones: {0}".format(zone))
            else:
                zone = Zone.objects.get(id=zone_id).__dict__
                logger.debug("ZONE int: {0}".format(zone))
        else:
            zone = Zone.objects.get(english_name=zone_id.lower()).__dict__
            logger.debug("ZONE string: {0}".format(zone))
        logger.debug('ADS: zoneID: {0}'.format(zone_id))
    except Exception:
        zone = None
        size = BannerSize.objects.get(pk=int(bset.BANNER_SIZE_ID))
        # Создание зоны и сайта если его еще не существует
        if not zone_id.isdigit():
            zone = Zone(
                english_name=zone_id.lower(),
                name=zone_id.lower(),
                size=size,
            )
            zone.save()
            zone = zone.__dict__

    if zone:
        request.session['user_mac'] = False
        placement = cache.get("banner_placement:{0}".format(zone["id"]))
        count = 0
        if not placement:
            try:
                placement = Placement.objects.filter(
                    (Q(begin_date__lte=dt.now()) | Q(begin_date__isnull=True)),
                    (Q(end_date__gte=dt.now()) | Q(end_date__isnull=True)),
                    (Q(max_clicks__gt=F('clicks')) | Q(max_clicks=0)),
                    (Q(max_shows__gt=F('shows')) | Q(max_shows=0)), zones__id=zone["id"]).select_related().order_by('-id').values()
                #if var:
                #    placement = placement.filter(var=var)
                #if varnot:
                #    placement = placement.exclude(var=varnot)
                cache.set("banner_placement:{0}".format(zone["id"]), list(placement), bset.BANNER_CACHE_TIME)
            except Exception:
                return u''

        count = len(placement)
        banner, plc = False, False

        if count == 1:
            plc = placement[0]
            logger.debug(u'ADS: placement[{1}] {0}'.format(plc, plc['id']))
            try:
                banners = Banner.objects.filter(campaign=plc['id'], size_id=zone['size_id'], is_active=True)
                banner = banners[0]
                logger.debug(u'ADS: banner[{0}] {1}'.format(banner.id, banner))
            except Exception:
                # TODO: баннер по умолчанию для зонны
                return u''
        elif count > 1:
            banners = [[t_p["banner_id"], t_p["frequency"], t_p] for t_p in placement]
            banner, plc = w_choice(normalize(banners))
        else:
            return u''

        if banner:
            request.banners_placement_shows.append(plc["id"])
            request.session['banner_type'] = banner.banner_type
            request.session['banner'] = banner.id
            # Кэшируем баннер
            #hbanner = cache.get("hbanner.{0}".format(banner.id))
            if not hbanner:
                #b = Banner.objects.get(pk=banner.id, is_active=True)
                #logger.debug("ZONE: {0}".format(zone))
                hbanner = gen_code(banner, plc, zone, request)
            #else:
            #    hbanner = u""
            #cache.set("hbanner.{0}".format(banner.id), hbanner, bset.BANNER_CACHE_TIME)
        return hbanner
    # Если зона не найдена
    else:
        return u""
