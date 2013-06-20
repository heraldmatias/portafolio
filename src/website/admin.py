# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from .models import Pagina, Contact


class PaginaAdmin(admin.ModelAdmin):
    list_display = ('tipo','creador',)
    list_display_links = ('tipo',)
    exclude = ['creador']

    def save_model(self, request, obj, form, change):
        obj.creador = request.user
        obj.save()

    #class Media:        
    #    js = ("tinymce/jscripts/tiny_mce/tiny_mce.js", "js/jscontenido.js")


class PortafolioFlatPageAdmin(FlatPageAdmin):

    class Media:
        js = ("tinymce/jscripts/tiny_mce/tiny_mce.js", "js/jscontenido.js")


class ContactAdmin(admin.ModelAdmin):

    list_display = ('person', 'subject', 'email', 'created')


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PortafolioFlatPageAdmin)
admin.site.register(Pagina,PaginaAdmin)
admin.site.register(Contact, ContactAdmin)