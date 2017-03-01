from django.conf.urls.static import static
from django.conf.urls import include, url

from .views import (
	#Other
	HomeView,
	ProductListView,
	#CRUD
	ProductCreateView,
	ProductDetailView,
	ProductUpdateView,
	ProductDeleteView
	)


urlpatterns = [
   url(r'^home/$', HomeView.as_view(), name='ecommerce_home'),
   url(r'^list/$', ProductListView.as_view(), name='product_list'),


   #########
   # CRUD  #
   #########
   #Create
   url(r'^create/$', ProductCreateView.as_view(), name='product_create'),
   #Read (Detail/Show)
   url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
   #Update
   url(r'^update/(?P<pk>\d+)/$', ProductUpdateView.as_view(), name='product_update'),
   #Delete
   url(r'^delete/(?P<pk>\d+)/$', ProductDeleteView.as_view(), name='product_delete'),
]
