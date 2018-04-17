from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Car

class IndexView(ListView):
    model = Car
    paginate_by = 3
    template_name = 'index.html'    
    
    # override of get_queryset
    def get_queryset(self):
        # return newest cars
        return Car.objects.order_by('-car_year')
    
    # override
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(IndexView, self).get_context_data(**kwargs)
        
        # add 3 newest picked cars to the context
        context['picked_cars'] = Car.objects.filter(car_picked = True).order_by('-car_year')[:3]
        
        return context
     
class DetailView(generic.DetailView):
    model = Car
    template_name = 'details.html'
