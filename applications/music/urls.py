from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


from .views import HomeView, AlbumListView
from .views import (
	AlbumCreateView,
	AlbumDetailView,
	AlbumUpdateView,
	AlbumDeleteView
	)


urlpatterns = [
   url(r'^home/$', HomeView.as_view(), name='album_home'),
   url(r'^list/$', AlbumListView.as_view(), name='album_list'),


   #########
   # CRUD  #
   #########
   #Create
   url(r'^create/$', AlbumCreateView.as_view(), name='album_create'),
   #Read (Detail/Show)
   url(r'^(?P<pk>\d+)/$', AlbumDetailView.as_view(), name='album_detail'),
   #Update
   url(r'^update/(?P<pk>\d+)/$', AlbumUpdateView.as_view(), name='album_update'),
   #Delete
   url(r'^delete/(?P<pk>\d+)/$', AlbumDeleteView.as_view(), name='album_delete'),
]
