# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from .models import Pagina


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo','tipo','creador',)
    list_display_links = ('titulo',)
    exclude = ['creador']

    def save_model(self, request, obj, form, change):
        obj.creador = request.user
        obj.save()

    class Media:        
        js = ("tinymce/jscripts/tiny_mce/tiny_mce.js", "js/jscontenido.js")


class PortafolioFlatPageAdmin(FlatPageAdmin):

    class Media:
        js = ("tinymce/jscripts/tiny_mce/tiny_mce.js", "js/jscontenido.js")

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PortafolioFlatPageAdmin)
admin.site.register(Pagina,PaginaAdmin)