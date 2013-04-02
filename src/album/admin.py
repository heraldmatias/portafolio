# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from django import forms

from .models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    exclude = ['slug']
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'order', )
    exclude = ['slug']
    list_editable = ['order', ]
    inlines = [
        PhotoInline,
    ]

admin.site.register(Album, AlbumAdmin)