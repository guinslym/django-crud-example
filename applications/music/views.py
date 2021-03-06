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
from .forms  import AlbumForm

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


class AlbumCreateView(SuccessMessageMixin, CreateView):
    form_class = AlbumForm
    template_name = "music/album_create.html"
    success_message = 'Successfully Added a Post entry'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.author = self.request.user
        return super(AlbumCreateView, self).form_valid(form)

album_new = login_required(AlbumCreateView.as_view())


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'music/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

album_detail = AlbumDetailView.as_view()

class AlbumUpdateView(SuccessMessageMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "music/album_create.html"
    success_message = 'Successfully Updated a Post entry'

    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        #self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

album_update = login_required(AlbumUpdateView.as_view())


class  AlbumDeleteView(SuccessMessageMixin, DeleteView):
    model = Album
    success_message = 'Successfully Deleted a Post entry'
    success_url = reverse_lazy('music:album_list')

    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
    	messages.success(self.request, self.success_message)
    	return super(self.__class__, self).delete(request, *args, **kwargs)
