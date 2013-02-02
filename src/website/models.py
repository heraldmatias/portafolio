# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from utils.clases import Enumeration


class Pagina(models.Model):

    TIPOS = Enumeration([
        (0, 'BIOGRAPHY', u'Biografía'),
        (1, 'PRESENT', u'Actualidad'),
    ])

    tipo = models.IntegerField(
                               verbose_name='Tipo pagina',
                               choices=TIPOS)
    titulo = models.CharField(
                              verbose_name='Título de la Pagina',
                              max_length=150)
    descripcion = models.CharField(
                                   verbose_name='Descripción de la Pagina',
                                   max_length=300)
    contenido = models.TextField(verbose_name='Contenido de la pagina')
    creador = models.ForeignKey(User)

    class Meta:
    	verbose_name = 'Pagina'
    	verbose_name_plural = 'Paginas'

    def __unicode__(self):
        return self.TIPOS.get_string(self.tipo)