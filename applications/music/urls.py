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
	AlbumUpdateView
	)


urlpatterns = [
   url(r'^home/$', HomeView.as_view(), name='music_home'),
   url(r'^list/$', AlbumListView.as_view(), name='music_list'),
   #########
   # CRUD  #
   #########
   #Create
   url(r'^create/$', AlbumCreateView.as_view(), name='music_create'),
   #Read (Detail)
   url(r'^(?P<pk>\d+)/$', AlbumDetailView.as_view(), name='album_detail'),
	#url(r'^lineup_post/(?P<pk>\d+)/$', lineupView.LineupDetailView.as_view(), name="post"),
]
