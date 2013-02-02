# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Pagina

class PaginaAdmin(admin.ModelAdmin):
    list_display = ('codigo','titulo','tipo','creador',)
    list_display_links = ('codigo','titulo',)
    exclude = ['creador']

    def save_model(self, request, obj, form, change):
        obj.creador = request.user
        obj.save()

    class Media:        
        js = ("tinymce/jscripts/tiny_mce/tiny_mce.js",
        	#"grappelli/tinymce_setup/tinymce_setup.js")
        	"js/jscontenido.js")

admin.site.register(Pagina,PaginaAdmin)