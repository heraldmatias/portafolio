# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

from .views import (IndexView, ContactCreateView, PresentView,
                    ContactSuccessView)

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='portafolio_index'),
    url(r'^actualidad/$', PresentView.as_view(), name='portafolio_actualidad'),
    url(r'^contacto/$', ContactCreateView.as_view(), name='portafolio_contacto'),
    url(r'^recibido/$', ContactSuccessView.as_view(), name='portafolio_recibido'),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^biografia/$',
        'flatpage',
        {'url': '/biografia/'},
        name='portafolio_biografia'),
)