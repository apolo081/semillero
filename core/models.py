#coding=UTF-8
from django.contrib.auth.models import User
from django.db import models
import choices
# Create your models here.

#USUARIOS DEL SISTEMA

class Coordinador(models.Model):
    user = models.OneToOneField(User,related_name='coordinador')
    codigo = models.CharField(max_length=15,verbose_name='código')

    class Meta:
        verbose_name = 'Coordinador'
        verbose_name_plural = 'Coordinadores'

    def __unicode__(self):
        return u'{0} {1}'.format(self.user.first_name,self.user.last_name)

class LiderGrupo(models.Model):
    user = models.OneToOneField(User,related_name='lidergrupo')
    codigo = models.CharField(max_length=15,verbose_name='código')

    class Meta:
        verbose_name = 'Lider_de_Grupo'
        verbose_name_plural = 'Lideres_de_Grupo'

    def __unicode__(self):
        return u'{0} {1}'.format(self.user.first_name,self.user.last_name)

class Estudiante(models.Model):
    user = models.OneToOneField(User,related_name='estudiante')
    codigo = models.CharField(max_length=15,verbose_name='código')
    semestre = models.IntegerField(choices = choices.semestres)
    programa = models.CharField(max_length=10, choices= choices.programas)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __unicode__(self):
        return u'{0} {1} : {2} {3}'.format(self.user.first_name,self.user.last_name,self.programa,self.semestre)
