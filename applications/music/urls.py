from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


from .views import HomeView, AlbumListView

urlpatterns = [
   url(r'^', HomeView.as_view(), name='music_home'),
   url(r'^list/$', AlbumListView.as_view(), name='music_list'),
	#url(r'^lineup_post/(?P<pk>\d+)/$', lineupView.LineupDetailView.as_view(), name="post"),
]
