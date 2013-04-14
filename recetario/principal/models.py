#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receta(models.Model):
    titulo = models.CharField(max_length=100, verbose_name = 'Titulo', unique = True)
    ingredientes  = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField()
    imagen = models.ImageField(upload_to = 'recetas',verbose_name = 'Imagen')
    tiempo_registro = models.DateTimeField(auto_now = True)
    usuario = models.ForeignKey(User)
    detalle  = models.TextField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    nro = models.IntegerField()

    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text = 'Tu comentario',verbose_name = 'Comentario')
    
    
    def __unicode_(self):
        return self.texto


class Producto(models.Model):
    codigo = models.BigIntegerField()
    descripcion = models.TextField(help_text = 'Descripcion del Producto',verbose_name = 'Descripcion')    
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    marca = models.TextField(help_text = 'Tu marca',verbose_name = 'Marca')
    modelo = models.TextField(help_text = 'Tu modelo',verbose_name = 'Modelo')
    opcion = models.BooleanField()
    sw = models.TextField()      
    
    def __unicode_(self):
        return self.texto    


class TblUsuario(models.Model):
    usr_alias = models.CharField(max_length=200, db_column=u'Usr_Alias') # Field name made lowercase.
    usr_tipopersona = models.CharField(max_length=200, db_column=u'Usr_TipoPersona') # Field name made lowercase.
    usr_nomcompleto = models.CharField(max_length=200, db_column=u'Usr_NomCompleto') # Field name made lowercase.
    usr_apellidopaterno = models.CharField(max_length=200, db_column=u'Usr_ApellidoPaterno') # Field name made lowercase.
    usr_apellidomaterno = models.CharField(max_length=200, db_column=u'Usr_ApellidoMaterno') # Field name made lowercase.
    usr_razonsocial = models.CharField(max_length=200, db_column=u'Usr_RazonSocial', blank=True) # Field name made lowercase.
    usr_tipodocumento = models.CharField(max_length=200, db_column=u'Usr_TipoDocumento') # Field name made lowercase.
    usr_nrodocumento = models.CharField(max_length=200, db_column=u'Usr_NroDocumento') # Field name made lowercase.
    usr_nrotelefono = models.CharField(max_length=200, db_column=u'Usr_NroTelefono', blank=True) # Field name made lowercase.
    usr_nrocelular = models.CharField(max_length=200, db_column=u'Usr_NroCelular', blank=True) # Field name made lowercase.
    usr_departamento = models.CharField(max_length=200, db_column=u'Usr_Departamento', blank=True) # Field name made lowercase.
    usr_provincia = models.CharField(max_length=200, db_column=u'Usr_Provincia', blank=True) # Field name made lowercase.
    usr_distrito = models.CharField(max_length=200, db_column=u'Usr_Distrito', blank=True) # Field name made lowercase.
    usr_direccion = models.CharField(max_length=200, db_column=u'Usr_Direccion', blank=True) # Field name made lowercase.
    usr_mail = models.CharField(max_length=100, db_column=u'Usr_Mail') # Field name made lowercase.
    usr_password = models.CharField(max_length=200, db_column=u'Usr_Password', blank=True) # Field name made lowercase.
   
        
class TblReclamo(models.Model):
    rec_tiporeclamo = models.CharField(max_length=200, db_column=u'Rec_TipoReclamo') # Field name made lowercase.
    rec_numero = models.CharField(max_length=200, db_column=u'Rec_Numero') # Field name made lowercase.
    rec_fecharegistro = models.DateTimeField(db_column=u'Rec_FechaRegistro') # Field name made lowercase.
    usr_alias = models.ForeignKey(TblUsuario, db_column=u'Usr_Alias') # Field name made lowercase.
    rec_descripcion = models.CharField(max_length=200, db_column=u'Rec_Descripcion') # Field name made lowercase.
    