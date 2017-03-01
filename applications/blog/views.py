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
from django.contrib.messages.views import SuccessMessageMixin

#django-friendship
#from friendship.models import Friend, Follow    

#models
from .models  import Article
from .forms  import ArticleForm

from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'blog/article_list.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        return Article.objects.all()#filter(status__iexact=Article.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)

article_list = ArticleListView.as_view()


class ArticleCreateView(SuccessMessageMixin, CreateView):
    form_class = ArticleForm
    template_name = "blog/article_create.html"
    success_message = 'Successfully Added a Post entry'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)

article_new = login_required(ArticleCreateView.as_view())

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

article_detail = ArticleDetailView.as_view()

class ArticleUpdateView(SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "music/article_create.html"
    success_message = 'Successfully Updated a Post entry'

    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        #self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

article_update = login_required(ArticleUpdateView.as_view())


class  ArticleDeleteView(SuccessMessageMixin, DeleteView):
    model = Article
    success_message = 'Successfully Deleted a Post entry'
    success_url = reverse_lazy('music:article_list')

    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
    	messages.success(self.request, self.success_message)
    	return super(self.__class__, self).delete(request, *args, **kwargs)
