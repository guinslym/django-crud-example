from django.conf.urls.static import static
from django.conf.urls import include, url

from .views import (
	#Other
	HomeView,
	#ArticleListView,
	#CRUD
	#ArticleCreateView,
	#ArticleDetailView,
	#ArticleUpdateView,
	#ArticleDeleteView
	)


urlpatterns = [
   url(r'^home/$', HomeView.as_view(), name='blog_home'),
   #url(r'^list/$', ArticleListView.as_view(), name='article_list'),


   #########
   # CRUD  #
   #########
   #Create
   #url(r'^create/$', ArticleCreateView.as_view(), name='article_create'),
   #Read (Detail/Show)
   #url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
   #Update
   #url(r'^update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name='article_update'),
   #Delete
   #url(r'^delete/(?P<pk>\d+)/$', ArticleDeleteView.as_view(), name='article_delete'),
]
