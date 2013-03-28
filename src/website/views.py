# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, CreateView
from django.core.urlresolvers import reverse

from album.models import Album

from .models import Pagina, Contact
from .forms import ContactForm


class IndexView(ListView):

    template_name = "website/index.html"
    model = Album

    def get_queryset(self):
        albums = Album.objects.all()[:12]
        return albums


class ContactCreateView(CreateView):

    model = Contact
    form_class = ContactForm
    template_name = "website/contact.html"
    success_url = "/recibido/"


class ContactSuccessView(TemplateView):

    template_name = "website/contact_success.html"


class PresentView(TemplateView):
    template_name = "actualidad.html"


class InternalErrorView(TemplateView):
    template_name = "500.html"
