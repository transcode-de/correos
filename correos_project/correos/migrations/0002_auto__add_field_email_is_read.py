# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Email.is_read'
        db.add_column(u'correos_email', 'is_read',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Email.is_read'
        db.delete_column(u'correos_email', 'is_read')


    models = {
        u'correos.domain': {
            'Meta': {'object_name': 'Domain'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'})
        },
        u'correos.email': {
            'Meta': {'ordering': "['-date']", 'unique_together': "(('message_id', 'recipient'),)", 'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'header': ('django.db.models.fields.TextField', [], {}),
            'is_multipart': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emails'", 'to': u"orm['correos.Recipient']"}),
            'sender': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'})
        },
        u'correos.recipient': {
            'Meta': {'ordering': "['domain', 'email']", 'object_name': 'Recipient'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users'", 'to': u"orm['correos.Domain']"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'realname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'primary_key': 'True'})
        }
    }

    complete_apps = ['correos']