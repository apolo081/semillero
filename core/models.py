#coding=UTF-8
from django.contrib.auth.models import User
from django.db import models
import choices
import utils
# Create your models here.

#USUARIOS DEL SISTEMA

class Coordinador(models.Model):
    user = models.OneToOneField(User,related_name='Coordinador')
    codigo = models.CharField(max_length=15,verbose_name='Código')

    class Meta:
        verbose_name = 'Coordinador'
        verbose_name_plural = 'Coordinadores'

    def __unicode__(self):
        return u'{0} {1}'.format(self.user.first_name,self.user.last_name)

class LiderGrupo(models.Model):
    user = models.OneToOneField(User,related_name='Lidergrupo')
    codigo = models.CharField(max_length=15,verbose_name='Código')

    class Meta:
        verbose_name = 'Líder de Grupo'
        verbose_name_plural = 'Líderes de Grupo'

    def __unicode__(self):
        return u'{0} {1}'.format(self.user.first_name,self.user.last_name)

class Estudiante(models.Model):
    user = models.OneToOneField(User,related_name='Estudiante')
    codigo = models.CharField(max_length=15,verbose_name='Código')
    semestre = models.IntegerField(choices = choices.semestres)
    programa = models.CharField(max_length=10, choices= choices.programas)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __unicode__(self):
        return u'{0} {1} : {2} {3}'.format(self.user.first_name,self.user.last_name,self.programa,self.semestre)


class Semillero(models.Model):
    nombre = models.CharField(max_length = 20, verbose_name='Semillero')
    programa = models.CharField(max_length=10, choices= choices.programas)
    logo = models.ImageField(upload_to='logos/')
    lider = models.ForeignKey('LiderGrupo')

    class Meta:
        verbose_name = 'Semillero'
        verbose_name_plural = 'Semilleros'

    def __unicode__(self):
        return u'{0} : {1} '.format(self.nombre,self.programa)

class Linea_investigacion(models.Model):
    nombre = models.CharField(max_length = 20, verbose_name='Linea investigación')
    semillero = models.ForeignKey('Semillero')

    class Meta:
        verbose_name = 'Línea investigación'
        verbose_name_plural = 'Líneas de investigación'

    def __unicode__(self):
        return u'{0} : {1} '.format(self.nombre,self.semillero)

class Articulo (models.Model):
    titulo = models.CharField(max_length= 20, verbose_name='Título Artículo')
    documento = models.FileField(upload_to= utils.content_file_name)
    estudiante = models.ForeignKey('Estudiante')
    semillero = models.ForeignKey('Semillero')
    revision = models.FloatField()
    estado = models.IntegerField(choices= choices.estado)

    class Meta:
        verbose_name = 'Título Artículo'
        verbose_name_plural = 'Títulos de artículos'

    def __unicode__(self):
        return u'{0} {1} {2} {3}'.format(self.titulo,self.semillero,self.estudiante,self.estado)

class Anotacion (models.Model):
    articulo = models.ForeignKey('Articulo')
    lider = models.ForeignKey('LiderGrupo')
    fecha_anotacion = models.DateField(auto_now= True)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Anotación'
        verbose_name_plural = 'Anotaciones'

    def __unicode__(self):
        return u'{0}'.format(self.articulo)

