# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Zone, Banner, Placement, BannerSize, BannerShow, BannerClick
from .utils import clear_banners_cache
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.admin import AdminImageMixin, AdminInlineImageMixin


class BannerSizeAdmin(admin.ModelAdmin):
    list_display = ("name", "get_size")


class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "english_name", 'author', 'size', 'is_active')
    list_per_page = 30
    prepopulated_fields = {'english_name': ('name',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(ZoneAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def save_model(self, request, obj, form, change):
        clear_banners_cache()
        obj.save()


class BannerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'banner_type', 'campaign', 'is_active')
        }),
        (_(u"Параметры"), {
            'classes': ('wide',),
            'fields': ('foreign_url', 'size')
        }),
        (None, {
            'classes': ('wide',),
            'fields': ('swf_file', 'img_file', 'html_text', 'url_target')
        }),
        (None, {
            'classes': ('wide',),
            'fields': ('var', 'priority')
        })
    )
    list_display = ("name", "banner_type", "size", 'priority', 'is_active')
    list_per_page = 30

    def save_model(self, request, obj, form, change):
        clear_banners_cache()
        obj.save()


class InlineBannerAdmin(AdminInlineImageMixin, admin.TabularInline):
    model = Banner
    fieldsets = ((None, {'classes': ('wide',), 'fields': ['name', 'banner_type', 'foreign_url', 'size', 'priority',
                                                          'campaign']}),
                 (_(u"Баннер"), {'classes': ('wide',), 'fields': ['is_active', 'img_file', 'swf_file', 'var',
                                                                  'url_target']}))
    #raw_id_fields = ('user', )
    extra = 0


class PlacementAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'author', 'zones', 'frequency', 'priority', 'is_active')
        }),
        (u"Клики", {
            'classes': ('wide',),
            'fields': ('clicks', 'max_clicks')
        }),
        (u"Показы", {
            'classes': ('wide',),
            'fields': ('shows', 'max_shows')
        }),
        (u"Период размещения", {
            'classes': ('wide',),
            'fields': ('begin_date', 'end_date')
        })
    )
    #search_fields = ("banner__name",)
    #inlines = [InlineBannerAdmin]
    list_display = ("author", "get_zones", "frequency", "clicks", "max_clicks", "shows", "max_shows",
                    "begin_date", "end_date", "get_status", 'is_active', 'created_at')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(PlacementAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def save_model(self, request, obj, form, change):
        clear_banners_cache()
        obj.save()


class BannerShowAdmin(admin.ModelAdmin):
    readonly_fields = ('ses', 'user_mac', 'campaign', 'banner', 'zone', 'ip', 'referrer')
    #fieldsets = (
    #    (None, {
    #        'classes': ('wide',),
    #        'fields': ('campaign', 'banner', 'zone', 'datetime', 'ip', 'referrer', 'user_agent')
    #    }),
    #    (u"Период размещения", {
    #        'classes': ('wide',),
    #        'fields': ('begin_date', 'end_date')
    #    })
    #)
    list_display = ('client', 'ip', 'campaign', 'banner', 'zone', 'datetime')
    list_per_page = 30


class BannerClickAdmin(admin.ModelAdmin):
    readonly_fields = ('ses', 'user_mac', 'campaign', 'banner', 'zone', 'ip', 'referrer')
    #fieldsets = (
    #    (None, {
    #        'classes': ('wide',),
    #        'fields': ('campaign', 'banner', 'zone', 'datetime', 'ip', 'referrer', 'user_agent')
    #    }),
    #    (u"Период размещения", {
    #        'classes': ('wide',),
    #        'fields': ('begin_date', 'end_date')
    #    })
    #)
    list_display = ('ip', 'campaign', 'banner', 'zone', 'datetime')
    list_per_page = 30


admin.site.register(BannerShow, BannerShowAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(Placement, PlacementAdmin)
admin.site.register(BannerSize, BannerSizeAdmin)
admin.site.register(BannerClick, BannerClickAdmin)