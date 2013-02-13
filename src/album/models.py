# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Album(models.Model):

    name = models.CharField(_(u'Nombre'), max_length=250)
    slug = models.SlugField()
    description = models.TextField(_(u'Descipción'), blank=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    def get_cover_photo(self):
        photo = self.photo_set.get(is_cover=True)
        return photo


class Photo(models.Model):

    album = models.ForeignKey(Album)
    title = models.CharField(_(u'Título'), max_length=250)
    slug = models.SlugField()
    photo = models.ImageField(_(u'Foto'), upload_to='fotos/')
    description = models.TextField(_(u'Descipción'), blank=True)
    is_cover = models.BooleanField(_(u'Portada'), default=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Photo, self).save(*args, **kwargs)