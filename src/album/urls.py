# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import AlbumListView, AlbumDetailView, CategoryListView

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
                       url(r'^portafolio/categoria/(?P<category>[-\w]+)/$',
                           AlbumListView.as_view(),
                           name='portafolio_albumes_category'),
                       url(r'^portafolio/categoria/(?P<category>[-\w]+)/(?P<page>[-\d]+)/$',
                           AlbumListView.as_view(),
                           name='portafolio_albumes_category_page'),
                       url(r'^portafolio/album/(?P<slug>[-\w]+)/$',
                           AlbumDetailView.as_view(),
                           name='portafolio_album'),
                       url(r'^portafolio/categoria/$',
                           CategoryListView.as_view(),
                           name='portafolio_categories'),
                       url(r'^portafolio/categoria/(?P<page>[-\d]+)/$',
                           CategoryListView.as_view(),
                           name='portafolio_categories_page'),
)