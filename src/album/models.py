# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(_(u'Nombre'), max_length=30)
    slug = models.SlugField(null=True)
    description = models.TextField(_(u'Descipción'), blank=True)
    photo = models.ImageField(_(u'Foto'), upload_to='categoria/')
    order = models.IntegerField(_(u'Orden'))

    def __unicode__(self):
        return u'%s' % self.name

    def get_cover_photo(self):
        return self.photo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['order']
        verbose_name = _(u'Categoría')
        verbose_name_plural = _(u'Categorías')


class Album(models.Model):
    name = models.CharField(_(u'Nombre'), max_length=250)
    slug = models.SlugField()
    description = models.TextField(_(u'Descipción'), blank=True)
    order = models.IntegerField(_(u'Orden'))
    tags = models.TextField(u'Palabras Claves (TAGS)', help_text=u'Ingrese las palabras claves separadas por comas.')
    slug_tags = models.TextField(u'Slugify tags', blank=True, null=True)
    category = models.ForeignKey(Category, null=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Album"
        verbose_name_plural = _(u'Albumes')

    def __unicode__(self):
        return self.name

    def slice_tags(self):
        if self.tags:
            return [(t.strip(), slugify(t.strip()))
                    for t in self.tags.split(',') if not t.strip() == '']
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
            try:
                photo = self.photo_set.all()[0]
            except:
                pass
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