# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Receta.nro'
        db.add_column('principal_receta', 'nro',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Receta.nro'
        db.delete_column('principal_receta', 'nro')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'principal.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Receta']"}),
            'texto': ('django.db.models.fields.TextField', [], {})
        },
        'principal.producto': {
            'Meta': {'object_name': 'Producto'},
            'codigo': ('django.db.models.fields.BigIntegerField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.TextField', [], {}),
            'modelo': ('django.db.models.fields.TextField', [], {}),
            'opcion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'sw': ('django.db.models.fields.TextField', [], {})
        },
        'principal.receta': {
            'Meta': {'object_name': 'Receta'},
            'detalle': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ingredientes': ('django.db.models.fields.TextField', [], {}),
            'nro': ('django.db.models.fields.IntegerField', [], {}),
            'preparacion': ('django.db.models.fields.TextField', [], {}),
            'tiempo_registro': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'principal.tblreclamo': {
            'Meta': {'object_name': 'TblReclamo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rec_descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Rec_Descripcion'"}),
            'rec_fecharegistro': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'Rec_FechaRegistro'"}),
            'rec_numero': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Rec_Numero'"}),
            'rec_tiporeclamo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Rec_TipoReclamo'"}),
            'usr_alias': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.TblUsuario']", 'db_column': "u'Usr_Alias'"})
        },
        'principal.tblusuario': {
            'Meta': {'object_name': 'TblUsuario'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usr_alias': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_Alias'"}),
            'usr_apellidomaterno': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_ApellidoMaterno'"}),
            'usr_apellidopaterno': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_ApellidoPaterno'"}),
            'usr_departamento': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_Departamento'", 'blank': 'True'}),
            'usr_direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_Direccion'", 'blank': 'True'}),
            'usr_distrito': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_Distrito'", 'blank': 'True'}),
            'usr_mail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Usr_Mail'"}),
            'usr_nomcompleto': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_NomCompleto'"}),
            'usr_nrocelular': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_NroCelular'", 'blank': 'True'}),
            'usr_nrodocumento': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_NroDocumento'"}),
            'usr_nrotelefono': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_NroTelefono'", 'blank': 'True'}),
            'usr_password': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_Password'", 'blank': 'True'}),
            'usr_provincia': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_Provincia'", 'blank': 'True'}),
            'usr_razonsocial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_RazonSocial'", 'blank': 'True'}),
            'usr_tipodocumento': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_TipoDocumento'"}),
            'usr_tipopersona': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "u'Usr_TipoPersona'"})
        }
    }

    complete_apps = ['principal']