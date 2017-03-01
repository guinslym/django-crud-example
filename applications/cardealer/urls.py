from django.conf.urls.static import static
from django.conf.urls import include, url

from .views import (
	#Other
	HomeView,
	CarListView,
	#CRUD
	CarCreateView,
	CarDetailView,
	CarUpdateView,
	CarDeleteView
	)


urlpatterns = [
   url(r'^home/$', HomeView.as_view(), name='cardealer_home'),
   url(r'^list/$', CarListView.as_view(), name='car_list'),


   #########
   # CRUD  #
   #########
   #Create
   url(r'^create/$', CarCreateView.as_view(), name='car_create'),
   #Read (Detail/Show)
   url(r'^(?P<pk>\d+)/$', CarDetailView.as_view(), name='car_detail'),
   #Update
   url(r'^update/(?P<pk>\d+)/$', CarUpdateView.as_view(), name='car_update'),
   #Delete
   url(r'^delete/(?P<pk>\d+)/$', CarDeleteView.as_view(), name='car_delete'),
]
