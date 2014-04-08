# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LeaveMessage.phone'
        db.alter_column(u'query_parser_leavemessage', 'phone', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):

        # Changing field 'LeaveMessage.phone'
        db.alter_column(u'query_parser_leavemessage', 'phone', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'query_parser.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'query_parser.entity': {
            'Meta': {'object_name': 'Entity'},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'wiki_page': ('django.db.models.fields.URLField', [], {'max_length': '512'})
        },
        u'query_parser.leavemessage': {
            'Meta': {'object_name': 'LeaveMessage'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'query_parser.verb': {
            'Meta': {'object_name': 'Verb'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['query_parser.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['query_parser']