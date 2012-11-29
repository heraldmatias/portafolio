# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

TIPOS =(
    (1,'BIOGRAFIA'),
    (2,'ACTUALIDAD')
)

class Pagina(models.Model):
    codigo = models.AutoField(primary_key=True)
    tipo = models.IntegerField(verbose_name='Tipo pagina', choices=TIPOS,unique=True)
    titulo = models.CharField(verbose_name='Titulo de la Pagina', max_length=150)
    descripcion = models.CharField(verbose_name='Breve descripcion de la Pagina', max_length=300)
    contenido = models.TextField(verbose_name='Contenido de la pagina')
    creador = models.ForeignKey(User)

    def __unicode__(self):
    	return u'%s' % TIPOS[self.tipo-1][1]

    class Meta:
    	verbose_name = 'Pagina'
    	verbose_name_plural = 'Paginas'