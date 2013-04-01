# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse

from album.models import Album

from .models import Pagina, Contact
from .forms import ContactForm

def get_initial_data():
    piepagina = descripcion = tags = None
    try:
        secciones = Pagina.objects.all().order_by('tipo').values('contenido')
        print secciones
        piepagina = secciones[0]['contenido']        
        descripcion = secciones[1]['contenido']
        tags = secciones[2]['contenido']
    except:
        pass
    data = {
        'piepagina' : piepagina,
        'descripcion' : descripcion,
        'tags' : tags,
    }
    return data

class IndexView(ListView):

    template_name = "website/index.html"
    model = Album

    def get_queryset(self):
        albums = Album.objects.all()[:12]
        return albums

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(get_initial_data())
        return context

class ContactCreateView(CreateView):

    model = Contact
    form_class = ContactForm
    template_name = "website/contact.html"
    success_url = "/recibido/"

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context.update(get_initial_data())
        return context

class ContactSuccessView(TemplateView):

    template_name = "website/contact_success.html"

    def get_context_data(self, **kwargs):
        context = super(ContactSuccessView, self).get_context_data(**kwargs)
        context.update(get_initial_data())
        return context

class PresentView(TemplateView):
    template_name = "actualidad.html"


class InternalErrorView(TemplateView):
    template_name = "500.html"
