# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Skill.is_marketable'
        db.add_column(u'bid_platform_skill', 'is_marketable',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Skill.num_endorsements'
        db.add_column(u'bid_platform_skill', 'num_endorsements',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Skill.price'
        db.add_column(u'bid_platform_skill', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Skill.is_marketable'
        db.delete_column(u'bid_platform_skill', 'is_marketable')

        # Deleting field 'Skill.num_endorsements'
        db.delete_column(u'bid_platform_skill', 'num_endorsements')

        # Deleting field 'Skill.price'
        db.delete_column(u'bid_platform_skill', 'price')


    models = {
        u'bid_platform.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_marketable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'num_endorsements': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['bid_platform']