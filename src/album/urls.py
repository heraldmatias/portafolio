# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

from .views import AlbumListView, AlbumDetailView

urlpatterns = patterns('',
    url(r'^portafolio/$', AlbumListView.as_view(), name='portafolio_albumes'),
    url(r'^portafolio/tags/(?P<tags>[-\w]+)/$', 
    	AlbumListView.as_view(),
    	name='portafolio_albumes-tags'),
    url(r'^portafolio/tags/(?P<tags>[-\w]+)/(?P<page>[-\d]+)/$', 
    	AlbumListView.as_view(),
    	name='portafolio_albumes-tags-page'),
    url(r'^portafolio/(?P<page>[-\d]+)/$',
    	AlbumListView.as_view(),
    	name='portafolio_albumes_page'),
    url(r'^portafolio/(?P<slug>[-\w]+)/$',
        AlbumDetailView.as_view(),
        name='portafolio_album'),
)