# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Domain'
        db.create_table(u'correos_domain', (
            ('uuid', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'correos', ['Domain'])

        # Adding model 'Recipient'
        db.create_table(u'correos_recipient', (
            ('uuid', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('realname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(related_name='users', to=orm['correos.Domain'])),
        ))
        db.send_create_signal(u'correos', ['Recipient'])

        # Adding model 'Email'
        db.create_table(u'correos_email', (
            ('uuid', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, primary_key=True)),
            ('message_id', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('sender', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emails', to=orm['correos.Recipient'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_multipart', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('header', self.gf('django.db.models.fields.TextField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'correos', ['Email'])

        # Adding unique constraint on 'Email', fields ['message_id', 'recipient']
        db.create_unique(u'correos_email', ['message_id', 'recipient_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Email', fields ['message_id', 'recipient']
        db.delete_unique(u'correos_email', ['message_id', 'recipient_id'])

        # Deleting model 'Domain'
        db.delete_table(u'correos_domain')

        # Deleting model 'Recipient'
        db.delete_table(u'correos_recipient')

        # Deleting model 'Email'
        db.delete_table(u'correos_email')


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