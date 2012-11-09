#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)        
        return context

class BiographyView(TemplateView):
    template_name = "biografia.html"

    def get_context_data(self, **kwargs):
        context = super(BiographyView, self).get_context_data(**kwargs)        
        return context

class ContactView(TemplateView):
    template_name = "contacto.html"

class PortfolioView(TemplateView):
    template_name = "portafolio.html"

class PresentView(TemplateView):
    template_name = "actualidad.html"