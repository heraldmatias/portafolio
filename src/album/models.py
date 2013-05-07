# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Album(models.Model):

    name = models.CharField(_(u'Nombre'), max_length=250)
    slug = models.SlugField()
    description = models.TextField(_(u'Descipción'), blank=True)
    order = models.IntegerField(_(u'Orden'))
    tags = models.TextField(u'Palabras Claves (TAGS)', help_text=u'Ingrese las palabras claves separadas por comas.')
    slug_tags = models.TextField(u'Slugify tags', blank=True, null=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __unicode__(self):
        return self.name

    def slice_tags(self):
        if self.tags:
            return [ (t.strip(),slugify(t.strip())) 
            for t in self.tags.split(',') if not t.strip() == '' ]
        return []

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.slug_tags = slugify(self.tags)
        super(Album, self).save(*args, **kwargs)

    def get_cover_photo(self):
        photo = None
        try:
            photo = self.photo_set.filter(is_cover=True)[0]
        except:
            photo = self.photo_set.all()[0]
        return photo


class Photo(models.Model):

    album = models.ForeignKey(Album)
    title = models.CharField(_(u'Título'), max_length=250, blank=True)
    slug = models.SlugField()
    photo = models.ImageField(_(u'Foto'), upload_to='fotos/')
    description = models.TextField(_(u'Descipción'), blank=True)
    order = models.IntegerField(_(u'Orden'))
    is_cover = models.BooleanField(_(u'Portada'), default=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Photo, self).save(*args, **kwargs)