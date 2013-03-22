# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from django import forms

from .models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    exclude = ['slug']
    max_num = 12
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    exclude = ['slug']
    inlines = [
        PhotoInline,
    ]

admin.site.register(Album, AlbumAdmin)