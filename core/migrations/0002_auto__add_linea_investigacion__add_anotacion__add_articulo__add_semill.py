# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Linea_investigacion'
        db.create_table(u'core_linea_investigacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('semillero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Semillero'])),
        ))
        db.send_create_signal(u'core', ['Linea_investigacion'])

        # Adding model 'Anotacion'
        db.create_table(u'core_anotacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('articulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Articulo'])),
            ('lider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.LiderGrupo'])),
            ('fecha_anotacion', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Anotacion'])

        # Adding model 'Articulo'
        db.create_table(u'core_articulo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('documento', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('estudiante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Estudiante'])),
            ('semillero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Semillero'])),
            ('revision', self.gf('django.db.models.fields.FloatField')()),
            ('estado', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['Articulo'])

        # Adding model 'Semillero'
        db.create_table(u'core_semillero', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('programa', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('lider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.LiderGrupo'])),
        ))
        db.send_create_signal(u'core', ['Semillero'])


    def backwards(self, orm):
        # Deleting model 'Linea_investigacion'
        db.delete_table(u'core_linea_investigacion')

        # Deleting model 'Anotacion'
        db.delete_table(u'core_anotacion')

        # Deleting model 'Articulo'
        db.delete_table(u'core_articulo')

        # Deleting model 'Semillero'
        db.delete_table(u'core_semillero')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.anotacion': {
            'Meta': {'object_name': 'Anotacion'},
            'articulo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Articulo']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_anotacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.LiderGrupo']"})
        },
        u'core.articulo': {
            'Meta': {'object_name': 'Articulo'},
            'documento': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'estudiante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Estudiante']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revision': ('django.db.models.fields.FloatField', [], {}),
            'semillero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Semillero']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'core.coordinador': {
            'Meta': {'object_name': 'Coordinador'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Coordinador'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'core.estudiante': {
            'Meta': {'object_name': 'Estudiante'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programa': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Estudiante'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'core.lidergrupo': {
            'Meta': {'object_name': 'LiderGrupo'},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Lidergrupo'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'core.linea_investigacion': {
            'Meta': {'object_name': 'Linea_investigacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'semillero': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Semillero']"})
        },
        u'core.semillero': {
            'Meta': {'object_name': 'Semillero'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.LiderGrupo']"}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'programa': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['core']