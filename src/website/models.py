# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from utils.classes import Enumeration


class Pagina(models.Model):

    TIPOS = Enumeration([
        (0, 'BIOGRAPHY', u'Pie de Pagina'),        
    ])

    tipo = models.IntegerField(
                               verbose_name='Tipo pagina',
                               choices=TIPOS, unique=True)    
    contenido = models.TextField(verbose_name='Contenido de la pagina')
    creador = models.ForeignKey(User)

    class Meta:
    	verbose_name = 'Sección de Pagina'
    	verbose_name_plural = 'Secciones de Pagina'

    def __unicode__(self):
        return self.TIPOS.get_string(self.tipo)

    def type(self):
        return self.TIPOS.get_string(self.tipo)


class Contact(models.Model):

    person = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __unicode__(self):
        return u"Mesanje de: %s, con el asunto: %s" % (self.person, self.subject)

    def save(self, *args, **kwargs):
        super(Contact, self).save(*args,**kwargs)
        send_mail(self.subject, self.message, self.email, ['heraldmatias.oz@gmail.com'], fail_silently=False)