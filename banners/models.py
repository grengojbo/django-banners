# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime as dt
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.core.validators import MaxLengthValidator

try:
    from hashlib import md5
except ImportError:
    from md5 import md5
from time import time

BANNER_CODE = (
    (0, _(u'JavaScript')),
    (1, _(u'IFrame')),
    (2, _(u'WiFi Form javascript')),
    (3, _(u'Django Template')),
)
BANNER_TYPES = (
    ('g', _(u'графический баннер')),
    ('f', _(u'Flash-баннер')),
    ('h', _(u'HTML-баннер')),
    ('m', _(u'Mobile APP')),
    ('r', _(u'RSS or ATOM')),
    ('a', _(u'Adsense')),
    ('d', _(u'DoubleClick')),
    ('o', _(u'OpenX')),
)
PRIORITY = (
    (10, _(u'10 - Эксклюзивный')),
    (9, _(u'9 - Максимально высокий')),
    (8, _(u'8 - Очень высокий')),
    (7, _(u'7 - Высокий')),
    (6, _(u'6 - Выше среднего')),
    (5, _(u'5 - Средний')),
    (4, _(u'4 - Ниже среднего')),
    (3, _(u'3 - Низкий')),
    (2, _(u'2 - Очень низкий')),
    (1, _(u'1 - Максимально низкий')),
    (0, _(u'0 - Собственные кампании')),
)
URL_TARGET_CHOICES = (
    ('_self', _(u'Current page')),
    ('_blank', _(u'Blank page')),
)


def get_banner_upload_to(instance, filename):
    """
    Формирует путь для загрузки файлов
    """
    filename_parts = filename.split('.')
    ext = '.{0}'.format(filename_parts[-1]) if len(filename_parts) > 1 else ''
    new_filename = md5(u'{0}-{1}'.format(filename.encode('utf-8'), time())).hexdigest()
    return 'banner/{0}{1}'.format(new_filename, ext)


class BannerSize(models.Model):
    name = models.CharField(_(u"название"), max_length=255, null=False, blank=False)
    width = models.CharField(_(u"Ширина"), blank=True, default="", null=False, max_length=100,
                             help_text=_(u"После значения указывайте единицы, например 100px или 30%"))
    height = models.CharField(_(u"Высота"), blank=True, null=False, default="", max_length=100,
                              help_text=_(u"После значения указывайте единицы, например 100px или 30%"))

    class Meta(object):
        verbose_name = _(u"Размер баннера")
        verbose_name_plural = _(u"Размеры баннеров")
        ordering = ["name"]

    def get_size(self):
        return u"{0}x{1}".format(self.width, self.height)

    get_size.short_description = _(u'Размеры')
    get_size.allow_tags = True

    def __unicode__(self):
        return self.name


class Zone(models.Model):
    # Зона на сайте где будет отображатся баннер
    name = models.CharField(_(u"название"), max_length=255, blank=False, null=False)
    author = models.ForeignKey(User, verbose_name=_(u'Издатель'), default=1)
    #site = models.ForeignKey(Site, verbose_name=u"сайт", default=[settings.SITE_ID])
    size = models.ForeignKey(BannerSize, verbose_name=_(u'Размер'))
    english_name = models.CharField(_(u"название по-английски"), max_length=255, blank=False, null=False, unique=True,
                                    db_index=True)
    html_pre_banner = models.CharField(_(u"HTML перед баннером"), max_length=255, blank=True, default="")
    html_after_banner = models.CharField(_(u"HTML после баннера"), max_length=255, blank=True, default="")
    description = models.CharField(max_length=255, verbose_name=u"описание", blank=True, null=True)
    code_view = models.PositiveSmallIntegerField(verbose_name=_(u"Генератор кода"), choices=BANNER_CODE, default=1,
                                                 help_text=_(u"Как генерировать код?"))
    is_active = models.BooleanField(_(u'Is active'), default=True)
    #price = models.IntegerField(verbose_name=u"Цена месяца показа")

    class Meta(object):
        verbose_name = _(u"зона")
        verbose_name_plural = _(u"зоны")
        ordering = ["name"]

    def __unicode__(self):
        return u'{0}'.format(self.name)

    @property
    def width(self):
        return self.size.width

    @property
    def height(self):
        return self.size.height

        #def get_site(self):
        #    return u"{0} [{1}]".format(self.site.name, self.site)
        #get_site.short_description = _(u'Сайт')


class Campaign(models.Model):
    #client = models.ForeignKey(Client, verbose_name=_(u"Клиент"))
    name = models.CharField(max_length=100, verbose_name=_(u"Название"))
    begin_date = models.DateTimeField(verbose_name=_(u"Дата активации"), null=True, blank=True,
                                      help_text=_(u"Оставьте поле пустым, чтобы немедленно активировать кампанию"))
    end_date = models.DateTimeField(verbose_name=_(u"Дата деактивации"), null=True, blank=True,
                                    help_text=_(u"Оставьте поле пустым, чтобы кампания была активна всегда"))
    priority = models.IntegerField(verbose_name=_(u"Приоритет"), choices=PRIORITY)

    class Meta:
        #ordering = ["client__name", "name", ]
        verbose_name = _(u'кампания')
        verbose_name_plural = _(u'кампания')

    def __unicode__(self):
        #return u"{0} - {1}".format(self.client.name, self.name)
        return u"{0}".format(self.name)


class Placement(models.Model):
    name = models.CharField(_(u"название"), max_length=255, null=False, blank=False, default=u'')
    #banner = models.ForeignKey(Banner, verbose_name=_(u"баннер"))
    zones = models.ManyToManyField(Zone, verbose_name=_(u"зоны"), related_name="zones")
    frequency = models.PositiveIntegerField(_(u"частота"), blank=False, null=False, default=1,
                                            help_text=_(u"чем больше частота, тем чаще баннер будет показываться"))

    # Статистика
    clicks = models.PositiveIntegerField(_(u"Кликов"), blank=True, default=0)
    shows = models.PositiveIntegerField(_(u"Показов"), blank=True, default=0)
    # Ограничения
    max_clicks = models.PositiveIntegerField(_(u"Лимит кликов"), blank=True, default=0, null=False,
                                             help_text=_(u"0 - лимит не ограничен"))
    max_shows = models.PositiveIntegerField(_(u"Лимит показов"), blank=True, default=0, null=False,
                                            help_text=_(u"0 - лимит не ограничен"))
    begin_date = models.DateTimeField(_(u"Дата начала"), null=True, blank=True)
    end_date = models.DateTimeField(_(u"Дата окончания"), null=True, blank=True)
    var = models.CharField(max_length=255, verbose_name=_(u"Переменная"), blank=True, default="", null=True)
    comment = models.TextField(max_length=255, blank=True, verbose_name=_(u"Комментарий"), default="")
    author = models.ForeignKey(User, verbose_name=_(u'Рекламодатель'), blank=True, null=True)
    priority = models.PositiveSmallIntegerField(verbose_name=u"Приоритет", choices=PRIORITY, default=0)
    is_active = models.BooleanField(_(u'Is active'), default=True)
    created_at = models.DateTimeField(_(u'Create at'), auto_now_add=True, blank=True, null=True)

    class Meta(object):
        verbose_name = _(u"размещение")
        verbose_name_plural = _(u"размещения")
        #ordering = ["banner__name"]

    def view(self):
        self.shows = models.F('shows') + 1
        self.save()
        return ''

    def get_status(self):
        # Не активен
        if (self.max_clicks != 0 and self.max_clicks <= self.clicks) or \
                (self.max_shows != 0 and self.max_shows <= self.shows) or \
                (self.begin_date and self.begin_date > dt.now()) or \
                (self.end_date and self.end_date < dt.now()):
            return u"<span style=\"color:#ccc;\">Неактивен</span>"
        return u"<span style=\"color:green;\">Активен</span>"

    get_status.short_description = u"Статус"
    get_status.allow_tags = True

    def get_zones(self):
        zones = u"<ul>"
        for zone in self.zones.all():
            zones += u"<li>* {0}</li>".format(zone.name)
        zones += "</ul>"
        return zones

    get_zones.short_description = _(u"Зоны")
    get_zones.allow_tags = True

    def __unicode__(self):
        return u'bannerID:{0}'.format(self.pk)


class Banner(models.Model):
    campaign = models.ForeignKey(Placement, verbose_name=u"Кампания", blank=True, null=True, related_name='banners')
    #zones = models.ManyToManyField(Zone, verbose_name=u"Связанные зоны")
    name = models.CharField(_(u"название"), max_length=255, null=False, blank=False)
    banner_type = models.CharField(_(u"Тип баннера"), max_length=1, choices=BANNER_TYPES)
    # Внешний URL куда ведет баннер
    foreign_url = models.CharField(max_length=200, blank=True, verbose_name=_(u"URL перехода"), default="")
    #width = models.CharField(_(u"Ширина"), blank=True, default="", null=False, max_length=100,
    #                         help_text=_(u"После значения указывайте единицы, например 100px или 30%"))
    #height = models.CharField(_(u"Высота"), blank=True, null=False, default="", max_length=100,
    #                          help_text=_(u"После значения указывайте единицы, например 100px или 30%"))

    size = models.ForeignKey(BannerSize, verbose_name=_(u'Размер'), related_name='banners')

    # Прорабатываем баннеры
    swf_file = models.FileField(_(u"SWF файл"), upload_to=get_banner_upload_to, blank=True, null=True,
                                help_text=_(u"Только для Flash баннеров"))
    img_file = models.FileField(_(u"Изображение"), upload_to=get_banner_upload_to, blank=True,
                                help_text=_(u"Использовать для графических баннеров"), null=True)
    html_text = models.TextField(_(u"HTML текст"), blank=True, null=False, default="")
    alt = models.CharField(max_length=100, blank=True, verbose_name=u"alt текст", default="")
    comment = models.TextField(max_length=255, blank=True, verbose_name=u"Комментарий", default="")
    allow_template_tags = models.BooleanField(blank=True, null=False, default=False,
                                              verbose_name=u"Разрешены шаблонные тэги Django",
                                              help_text=u'Только для HTML баннеров. Разрешает использование в коде шаблонные тэги Django.')
    var = models.CharField(max_length=255, verbose_name=u"Переменная", blank=True, default="", null=True)
    priority = models.PositiveSmallIntegerField(verbose_name=u"Приоритет", choices=PRIORITY, default=0)
    is_active = models.BooleanField(_(u'Is active'), default=True)
    url_target = models.CharField(_(u'Target'), max_length=10, choices=URL_TARGET_CHOICES, default='')

    class Meta(object):
        verbose_name = _(u"баннер")
        verbose_name_plural = _(u"баннеры")
        ordering = ["name"]

    def __unicode__(self):
        return self.name

    @property
    def width(self):
        return self.size.width

    @property
    def height(self):
        return self.size.height

    def click(self, request):
        click = {
            'banner': self,
            'campaign': self.campaign,
            'ip': request.META.get('REMOTE_ADDR'),
            'user_agent': request.META.get('HTTP_USER_AGENT'),
            'referrer': request.META.get('HTTP_REFERER'),
        }

        if request.user.is_authenticated():
            click['user'] = request.user

        return BannerClick.objects.create(**click)


class BannerClick(models.Model):
    banner = models.ForeignKey(Banner, related_name="clicks")
    user = models.ForeignKey(User, null=True, blank=True, related_name="banner_clicks")
    #ses =
    user_mac = models.CharField(_(u'MAC адресс'), blank=True, null=True, max_length=17)
    campaign = models.ForeignKey(Placement, verbose_name=u"Кампания", blank=True, null=True,
                                 related_name='banner_clicks')
    datetime = models.DateTimeField("Clicked at", auto_now_add=True)
    ip = models.IPAddressField(null=True, blank=True)
    user_agent = models.TextField(validators=[MaxLengthValidator(1000)], null=True, blank=True)
    referrer = models.URLField(null=True, blank=True)


    #class Client(models.Model):
    #    name = models.CharField(max_length=100, verbose_name=u"Имя")
    #    contact = models.CharField(max_length=100, verbose_name=u"Контакт")
    #    email = models.EmailField(max_length=100, verbose_name=u"E-mail")
    #    one_banner_per_page = models.BooleanField(default=True, blank=True,
    #                                  verbose_name=u"Показывать только один баннер этого рекламодателя на странице")
    #
    #    class Meta:
    #        ordering = ["name", ]
    #        verbose_name = u"""клиент"""
    #        verbose_name_plural = u"""клиенты"""
    #
    #    def __unicode__(self):
    #        return self.name

    # https://github.com/mlavin/django-ad-code/blob/master/adcode/models.py
    #@receiver(post_save, sender=Placement)
    #def save_placement_handler(sender, instance,  **kwargs):
    #    "Add or update the placement in the caches."
    #    _update_placement_cache(placement=instance, replace=True)
    #
    #
    #@receiver(pre_delete, sender=Placement)
    #def delete_placement_handler(sender, instance,  **kwargs):
    #    "Remove the placement from the section caches."
    #    _update_placement_cache(placement=instance, replace=False)