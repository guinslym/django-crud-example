from django.conf.urls.static import static

from .views import (
   #Other
   HomeView,
   AlbumListView,
   #CRUD
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
