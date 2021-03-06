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
from .models  import Car
from .forms  import CarForm

from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'cardealer/car_list.html'


class CarListView(ListView):
    model = Car
    template_name = 'cardealer/car_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        return Car.objects.all()#filter(status__iexact=Car.STATUS.active)

    def get_paginate_by(self, queryset):
        """ Paginate by specified value in querystring, or use default class property value.  """
        return self.request.GET.get('paginate_by', self.paginate_by)

car_list = CarListView.as_view()


class CarCreateView(SuccessMessageMixin, CreateView):
    form_class = CarForm
    template_name = "cardealer/car_create.html"
    success_message = 'Successfully Added a Post entry'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.author = self.request.user
        return super(CarCreateView, self).form_valid(form)

car_new = login_required(CarCreateView.as_view())

class CarDetailView(DetailView):
    model = Car
    template_name = 'cardealer/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CarDetailView, self).get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

car_detail = CarDetailView.as_view()

class CarUpdateView(SuccessMessageMixin, UpdateView):
    model = Car
    form_class = CarForm
    template_name = "cardealer/car_create.html"
    success_message = 'Successfully Updated a Post entry'

    def dispatch(self, *args, **kwargs):
        return super(self.__class__, self).dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #migh need to remove that line
        #self.object.author = self.request.user
        return super(self.__class__, self).form_valid(form)

car_update = login_required(CarUpdateView.as_view())


class  CarDeleteView(SuccessMessageMixin, DeleteView):
    model = Car
    success_message = 'Successfully Deleted a Post entry'
    success_url = reverse_lazy('cardealer:car_list')

    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
    	messages.success(self.request, self.success_message)
    	return super(self.__class__, self).delete(request, *args, **kwargs)
