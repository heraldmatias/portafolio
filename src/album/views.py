# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView

from .models import Album, Category
from website.views import get_initial_data


class AlbumListView(ListView):
    template_name = "album/portafolio.html"
    model = Album
    paginate_by = 5

    def get_queryset(self):
        if 'tags' in self.kwargs:
            return Album.objects.filter(
                slug_tags__icontains=self.kwargs['tags'])
        if 'category' in self.kwargs:
            return Album.objects.filter(
                category__slug=self.kwargs['category'])
        return Album.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        context['tags'] = self.kwargs.get('tags', False)
        context['category'] = self.kwargs.get('category', False)
        context.update(get_initial_data())
        return context


class AlbumDetailView(DetailView):
    template_name = "album/album.html"
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context.update(get_initial_data())
        return context


class CategoryListView(ListView):
    template_name = "album/categories.html"
    model = Category
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context.update(get_initial_data())
        return context