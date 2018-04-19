from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.db.models import Q
from .models import Car
import functools
import operator

class IndexView(ListView):
    model = Car
    paginate_by = 10
    template_name = 'index.html' 
    
    # override of get_queryset
    def get_queryset(self):
        result = Car.objects.order_by('-car_year')

        # Handle description input, remove garbage        
        query = self.request.GET.get('desc')                     
        if query:
            value = ''.join(tok for tok in value if tok.isalnum() or tok == ' ')
            query_list = value.split()
            result = result.filter(
                functools.reduce(operator.and_,
                       (Q(car_make__icontains = q) for q in query_list))
            )
            
        # Handle carmake input              
        query = self.request.GET.get('carmake')            
        if query:            
            result = result.filter(Q(car_make__exact = query))
            
        # Handle carmodel input              
        query = self.request.GET.get('carmodel')            
        if query:                        
            result = result.filter(Q(car_model__exact = query))
            
        # Handle caryear input              
        query = self.request.GET.get('caryear')            
        if query:            
            query_list = query.split()
            result = result.filter(Q(car_year__exact = int(query)))
                                   
        # Handle carprice input              
        query = self.request.GET.get('carprice')            
        if query:      
            if int(query) == 1:                
                result = result.filter(Q(car_price__lte = 5000))
            elif int(query) == 2:                
                result = result.filter(Q(car_price__range = (5000, 10000)))
            elif int(query) == 3:                
                result = result.filter(Q(car_price__range = (10000, 15000)))
            else:
                result = result.filter(Q(car_price__gte = 15000))
                                       
        # Handle area zip input              
        query = self.request.GET.get('zip')            
        if query:            
            result = result.filter(Q(dealer_zip__exact = int(query)))
        
        # return cars
        return result
    
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
