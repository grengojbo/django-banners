# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BannerShow.ua_browser_family'
        db.add_column(u'banners_bannershow', 'ua_browser_family',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BannerShow.ua_browser_version'
        db.add_column(u'banners_bannershow', 'ua_browser_version',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BannerShow.ua_os_family'
        db.add_column(u'banners_bannershow', 'ua_os_family',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BannerShow.ua_os_version'
        db.add_column(u'banners_bannershow', 'ua_os_version',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BannerShow.ua_device_family'
        db.add_column(u'banners_bannershow', 'ua_device_family',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Placement.lim_weekday'
        db.add_column(u'banners_placement', 'lim_weekday',
                      self.gf('django.db.models.fields.CharField')(default='0, 1, 2, 3, 4, 5, 6', max_length=19),
                      keep_default=False)

        # Adding field 'Placement.lim_hour'
        db.add_column(u'banners_placement', 'lim_hour',
                      self.gf('django.db.models.fields.CharField')(default='0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23', max_length=84),
                      keep_default=False)

        # Adding field 'BannerClick.ua_browser_family'
        db.add_column(u'banners_bannerclick', 'ua_browser_family',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BannerClick.ua_browser_version'
        db.add_column(u'banners_bannerclick', 'ua_browser_version',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BannerClick.ua_os_family'
        db.add_column(u'banners_bannerclick', 'ua_os_family',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BannerClick.ua_os_version'
        db.add_column(u'banners_bannerclick', 'ua_os_version',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'BannerClick.ua_device_family'
        db.add_column(u'banners_bannerclick', 'ua_device_family',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BannerShow.ua_browser_family'
        db.delete_column(u'banners_bannershow', 'ua_browser_family')

        # Deleting field 'BannerShow.ua_browser_version'
        db.delete_column(u'banners_bannershow', 'ua_browser_version')

        # Deleting field 'BannerShow.ua_os_family'
        db.delete_column(u'banners_bannershow', 'ua_os_family')

        # Deleting field 'BannerShow.ua_os_version'
        db.delete_column(u'banners_bannershow', 'ua_os_version')

        # Deleting field 'BannerShow.ua_device_family'
        db.delete_column(u'banners_bannershow', 'ua_device_family')

        # Deleting field 'Placement.lim_weekday'
        db.delete_column(u'banners_placement', 'lim_weekday')

        # Deleting field 'Placement.lim_hour'
        db.delete_column(u'banners_placement', 'lim_hour')

        # Deleting field 'BannerClick.ua_browser_family'
        db.delete_column(u'banners_bannerclick', 'ua_browser_family')

        # Deleting field 'BannerClick.ua_browser_version'
        db.delete_column(u'banners_bannerclick', 'ua_browser_version')

        # Deleting field 'BannerClick.ua_os_family'
        db.delete_column(u'banners_bannerclick', 'ua_os_family')

        # Deleting field 'BannerClick.ua_os_version'
        db.delete_column(u'banners_bannerclick', 'ua_os_version')

        # Deleting field 'BannerClick.ua_device_family'
        db.delete_column(u'banners_bannerclick', 'ua_device_family')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'banners.banner': {
            'Meta': {'ordering': "['name']", 'object_name': 'Banner'},
            'allow_template_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'banner_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banners'", 'null': 'True', 'to': u"orm['banners.Placement']"}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'foreign_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'html_text': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banners'", 'to': u"orm['banners.BannerSize']"}),
            'swf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url_target': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'var': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'banners.bannerclick': {
            'Meta': {'object_name': 'BannerClick'},
            'audits': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clicks'", 'to': u"orm['banners.Banner']"}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner_clicks'", 'null': 'True', 'to': u"orm['banners.Placement']"}),
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'referrer': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ses': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'ua_browser_family': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ua_browser_version': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ua_device_family': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ua_os_family': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ua_os_version': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_mac': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'banner_clicks'", 'null': 'True', 'to': u"orm['banners.Zone']"})
        },
        u'banners.bannershow': {
            'Meta': {'object_name': 'BannerShow'},
            'audits': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banners.Banner']"}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banners.Placement']", 'null': 'True', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'referrer': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ses': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'shows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'ua_browser_family': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ua_browser_version': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ua_device_family': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ua_os_family': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ua_os_version': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user_mac': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banners.Zone']", 'null': 'True', 'blank': 'True'})
        },
        u'banners.bannersize': {
            'Meta': {'ordering': "['name']", 'object_name': 'BannerSize'},
            'height': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        },
        u'banners.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'begin_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        u'banners.placement': {
            'Meta': {'object_name': 'Placement'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'begin_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'client'", 'to': u"orm['auth.User']"}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lim_hour': ('django.db.models.fields.CharField', [], {'default': "'0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23'", 'max_length': '84'}),
            'lim_weekday': ('django.db.models.fields.CharField', [], {'default': "'0, 1, 2, 3, 4, 5, 6'", 'max_length': '19'}),
            'max_clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'max_shows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255'}),
            'one_banner_per_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'shows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'unique_mac': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique_session': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'var': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zones': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'zones'", 'symmetrical': 'False', 'to': u"orm['banners.Zone']"})
        },
        u'banners.resurce': {
            'Meta': {'ordering': "['name']", 'object_name': 'Resurce'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['imagestore.Album']", 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'author'", 'to': u"orm['auth.User']"})
        },
        u'banners.zone': {
            'Meta': {'ordering': "['name']", 'object_name': 'Zone'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['imagestore.Album']", 'null': 'True', 'blank': 'True'}),
            'code_view': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'english_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'html_after_banner': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'html_pre_banner': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'resurces': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banners.Resurce']", 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banners.BannerSize']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'imagestore.album': {
            'Meta': {'ordering': "('order', 'created', 'name')", 'object_name': 'Album'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'head': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'head_of'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['imagestore.Image']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'albums'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        'imagestore.image': {
            'Meta': {'ordering': "('order', 'id')", 'object_name': 'Image'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'images'", 'null': 'True', 'to': "orm['imagestore.Album']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'links': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'images'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['banners']