# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'BannerSize'
        db.create_table(u'banners_bannersize', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('width', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
        ))
        db.send_create_signal(u'banners', ['BannerSize'])

        # Adding model 'Zone'
        db.create_table(u'banners_zone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banners.BannerSize'])),
            ('english_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('html_pre_banner', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('html_after_banner', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'banners', ['Zone'])

        # Adding model 'Banner'
        db.create_table(u'banners_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('banner_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('foreign_url', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('width', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('height', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banners.BannerSize'])),
            ('swf_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('img_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('html_text', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', max_length=255, blank=True)),
            ('allow_template_tags', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('var', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'banners', ['Banner'])

        # Adding model 'Campaign'
        db.create_table(u'banners_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('begin_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'banners', ['Campaign'])

        # Adding model 'Placement'
        db.create_table(u'banners_placement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banners.Banner'])),
            ('frequency', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('clicks', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('shows', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('max_clicks', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('max_shows', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('begin_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('var', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'banners', ['Placement'])

        # Adding M2M table for field zones on 'Placement'
        m2m_table_name = db.shorten_name(u'banners_placement_zones')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('placement', models.ForeignKey(orm[u'banners.placement'], null=False)),
            ('zone', models.ForeignKey(orm[u'banners.zone'], null=False))
        ))
        db.create_unique(m2m_table_name, ['placement_id', 'zone_id'])


    def backwards(self, orm):
        # Deleting model 'BannerSize'
        db.delete_table(u'banners_bannersize')

        # Deleting model 'Zone'
        db.delete_table(u'banners_zone')

        # Deleting model 'Banner'
        db.delete_table(u'banners_banner')

        # Deleting model 'Campaign'
        db.delete_table(u'banners_campaign')

        # Deleting model 'Placement'
        db.delete_table(u'banners_placement')

        # Removing M2M table for field zones on 'Placement'
        db.delete_table(db.shorten_name(u'banners_placement_zones'))


    models = {
        u'banners.banner': {
            'Meta': {'ordering': "['name']", 'object_name': 'Banner'},
            'allow_template_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'banner_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'comment': (
            'django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'foreign_url': (
            'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'height': (
            'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'html_text': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_file': (
            'django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banners.BannerSize']"}),
            'swf_file': (
            'django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'var': ('django.db.models.fields.CharField', [],
                    {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        },
        u'banners.bannersize': {
            'Meta': {'ordering': "['name']", 'object_name': 'BannerSize'},
            'height': (
            'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
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
            'Meta': {'ordering': "['banner__name']", 'object_name': 'Placement'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banners.Banner']"}),
            'begin_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'comment': (
            'django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'max_shows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'shows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'var': ('django.db.models.fields.CharField', [],
                    {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zones': ('django.db.models.fields.related.ManyToManyField', [],
                      {'related_name': "'zones'", 'symmetrical': 'False', 'to': u"orm['banners.Zone']"})
        },
        u'banners.zone': {
            'Meta': {'ordering': "['name']", 'object_name': 'Zone'},
            'description': (
            'django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'english_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'html_after_banner': (
            'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'html_pre_banner': (
            'django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banners.BannerSize']"})
        }
    }

    complete_apps = ['banners']