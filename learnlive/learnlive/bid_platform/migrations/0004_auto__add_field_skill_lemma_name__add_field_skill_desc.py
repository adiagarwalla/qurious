# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Skill.lemma_name'
        db.add_column(u'bid_platform_skill', 'lemma_name',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=512),
                      keep_default=False)

        # Adding field 'Skill.desc'
        db.add_column(u'bid_platform_skill', 'desc',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Skill.lemma_name'
        db.delete_column(u'bid_platform_skill', 'lemma_name')

        # Deleting field 'Skill.desc'
        db.delete_column(u'bid_platform_skill', 'desc')


    models = {
        u'bid_platform.skill': {
            'Meta': {'object_name': 'Skill'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_marketable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lemma_name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'num_endorsements': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['bid_platform']