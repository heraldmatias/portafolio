# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Photo.order'
        db.add_column('album_photo', 'order', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Album.order'
        db.add_column('album_album', 'order', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Album.tags'
        db.add_column('album_album', 'tags', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Album.slug_tags'
        db.add_column('album_album', 'slug_tags', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Photo.order'
        db.delete_column('album_photo', 'order')

        # Deleting field 'Album.order'
        db.delete_column('album_album', 'order')

        # Deleting field 'Album.tags'
        db.delete_column('album_album', 'tags')

        # Deleting field 'Album.slug_tags'
        db.delete_column('album_album', 'slug_tags')


    models = {
        'album.album': {
            'Meta': {'ordering': "['order']", 'object_name': 'Album'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'slug_tags': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.TextField', [], {})
        },
        'album.photo': {
            'Meta': {'ordering': "['order']", 'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['album.Album']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_cover': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        }
    }

    complete_apps = ['album']
