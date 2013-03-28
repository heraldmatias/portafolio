# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView

from .models import Album


class AlbumListView(ListView):

    template_name = "album/portafolio.html"
    model = Album
    paginate_by = 5


class AlbumDetailView(DetailView):

    template_name = "album/album.html"
    model = Album