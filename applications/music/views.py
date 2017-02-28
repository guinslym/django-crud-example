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
from .models  import Album

#forms
#from .forms import ( ProductForm, ProductEditForm )

class HomeView(TemplateView):
    template_name = 'music/album_list.html'

class AlbumListView(ListView):
    model = Album
    template_name = 'music/album_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        return Album.objects.all()#filter(status__iexact=Article.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)

album_list = AlbumListView.as_view()

'''
class ProductCreateView(SuccessMessageMixin, CreateView):
    form_class = ProductForm
    template_name = "product_create.html"
    success_message = 'Successfully Added a Post entry'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super(ProductCreateView, self).form_valid(form)

product_new = login_required(ProductCreateView.as_view())

class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = "product_update.html"
    success_message = 'Successfully Updated a Post entry'

    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

product_edit = login_required(ProductUpdateView.as_view())


class  ProductDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Product
    template_name = '_delete_confirm.html'
    success_message = 'Successfully Deleted a Post entry'

    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['back_page'] = reverse_lazy('wadiyabi:product-home')
        return context

    def get_success_url(self):
        messages.success_message(self.request, 'Successfully Deleted Post entry')
        return reverse_lazy('wadiyabi:product-home')

product_delete = login_required(ProductDeleteView.as_view())



class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

product_detail = ProductDeleteView.as_view()

'''

