# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Zone, Banner, Placement, BannerSize, BannerShow, BannerClick, Resurce
from .utils import clear_banners_cache
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.admin import AdminImageMixin, AdminInlineImageMixin


class BannerSizeAdmin(admin.ModelAdmin):
    list_display = ("name", "get_size")


class InlineZoneAdmin(admin.TabularInline):
    model = Zone
    fieldsets = ((None, {'fields': ['name', 'size', 'code_view', 'is_active']}),)
    extra = 0


class ResurceAdmin(admin.ModelAdmin):
    list_display = ("name", "user", 'site', 'is_active', 'description')
    list_per_page = 30
    list_filter = ('is_active',)
    search_fields = ('name',)
    raw_id_fields = ('user',)
    inlines = [InlineZoneAdmin]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(ResurceAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )


class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "english_name", 'resurces', 'size', 'is_active')
    list_per_page = 30
    prepopulated_fields = {'english_name': ('name',)}
    list_filter = ('is_active',)
    search_fields = ('name',)
    raw_id_fields = ('resurces',)

    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #    if db_field.name == 'author':
    #        kwargs['initial'] = request.user.id
    #        return db_field.formfield(**kwargs)
    #    return super(ZoneAdmin, self).formfield_for_foreignkey(
    #        db_field, request, **kwargs
    #    )

    def save_model(self, request, obj, form, change):
        clear_banners_cache()
        obj.save()


class InlineBannerAdmin(AdminInlineImageMixin, admin.TabularInline):
    model = Banner
    fieldsets = ((None, {'fields': ['img_file', 'name', 'banner_type', 'foreign_url', 'size']}),)
    #raw_id_fields = ('user', )
    extra = 0


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
    list_filter = ('is_active',)

    def save_model(self, request, obj, form, change):
        clear_banners_cache()
        obj.save()


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
    inlines = [InlineBannerAdmin]
    list_display = ('name', "author", "get_zones", "frequency", "clicks", "max_clicks", "shows", "max_shows",
                    "begin_date", "end_date", "get_status", 'is_active', 'created_at')
    list_filter = ('is_active',)
    raw_id_fields = ('author',)
    search_fields = ('name',)

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
    readonly_fields = ('ses', 'user_mac', 'campaign', 'banner', 'zone', 'ip', 'shows', 'referrer', 'audits',
                       'datetime', 'user_agent')
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
    list_display = ('client', 'ip', 'campaign', 'banner', 'zone', 'datetime', 'audits')
    list_per_page = 30
    list_filter = ('audits',)
    date_hierarchy = 'datetime'


class BannerClickAdmin(admin.ModelAdmin):
    readonly_fields = ('ses', 'user_mac', 'campaign', 'banner', 'zone', 'ip', 'clicks', 'referrer', 'audits',
                       'datetime', 'user_agent')
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
    list_display = ('ip', 'campaign', 'banner', 'zone', 'datetime', 'audits')
    list_per_page = 30
    list_filter = ('audits',)
    date_hierarchy = 'datetime'


admin.site.register(BannerShow, BannerShowAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Zone, ZoneAdmin)
admin.site.register(Placement, PlacementAdmin)
admin.site.register(BannerSize, BannerSizeAdmin)
admin.site.register(BannerClick, BannerClickAdmin)
admin.site.register(Resurce, ResurceAdmin)