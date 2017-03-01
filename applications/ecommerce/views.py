from datetime import datetime
from django.core.urlresolvers import reverse, reverse_lazy

#Class Based View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Protected
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

#django-friendship
#from friendship.models import Friend, Follow    

#models
from .models  import Product
#from .forms  import ProductForm

from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'ecommerce/product_list.html'


class ProductListView(ListView):
    model = Product
    template_name = 'ecommerce/product_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        return Product.objects.all()#filter(status__iexact=Product.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)

product_list = ProductListView.as_view()


class ProductCreateView(SuccessMessageMixin, CreateView):
    form_class = ProductForm
    template_name = "ecommerce/product_create.html"
    success_message = 'Successfully Added a Post entry'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.author = self.request.user
        return super(ProductCreateView, self).form_valid(form)

product_new = login_required(ProductCreateView.as_view())

class ProductDetailView(DetailView):
    model = Product
    template_name = 'ecommerce/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

product_detail = ProductDetailView.as_view()

class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "ecommerce/product_create.html"
    success_message = 'Successfully Updated a Post entry'

    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        #self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

product_update = login_required(ProductUpdateView.as_view())


class  ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    success_message = 'Successfully Deleted a Post entry'
    success_url = reverse_lazy('ecommerce:product_list')

    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
    	messages.success(self.request, self.success_message)
    	return super(self.__class__, self).delete(request, *args, **kwargs)
