# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView

from album.models import Album
from .models import Pagina


class IndexView(ListView):

    template_name = "website/index.html"
    model = Album

    def get_queryset(self):
        albums = Album.objects.all()[:5]
        return albums


class ContactView(TemplateView):
    template_name = "contacto.html"


class PortfolioView(TemplateView):
    template_name = "portafolio.html"


class PresentView(TemplateView):
    template_name = "actualidad.html"


class InternalErrorView(TemplateView):
    template_name = "500.html"
