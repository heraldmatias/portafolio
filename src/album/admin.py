# -*- coding: utf-8 -*-
from album.models import Category

from django.contrib import admin

from .models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    exclude = ['slug']
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'order', )
    exclude = ['slug', 'slug_tags']
    list_editable = ['order', ]
    inlines = [
        PhotoInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'photo', 'description')
    exclude = ['slug']
    list_editable = ['name', 'order', 'photo', 'description']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Category, CategoryAdmin)