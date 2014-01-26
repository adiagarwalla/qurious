# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'query_parser_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'query_parser', ['Category'])

        # Adding model 'Verb'
        db.create_table(u'query_parser_verb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'query_parser', ['Verb'])

        # Adding M2M table for field categories on 'Verb'
        m2m_table_name = db.shorten_name(u'query_parser_verb_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('verb', models.ForeignKey(orm[u'query_parser.verb'], null=False)),
            ('category', models.ForeignKey(orm[u'query_parser.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['verb_id', 'category_id'])

        # Adding model 'Entity'
        db.create_table(u'query_parser_entity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('numchild', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('wiki_page', self.gf('django.db.models.fields.URLField')(max_length=512)),
        ))
        db.send_create_signal(u'query_parser', ['Entity'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'query_parser_category')

        # Deleting model 'Verb'
        db.delete_table(u'query_parser_verb')

        # Removing M2M table for field categories on 'Verb'
        db.delete_table(db.shorten_name(u'query_parser_verb_categories'))

        # Deleting model 'Entity'
        db.delete_table(u'query_parser_entity')


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
        u'query_parser.verb': {
            'Meta': {'object_name': 'Verb'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['query_parser.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['query_parser']