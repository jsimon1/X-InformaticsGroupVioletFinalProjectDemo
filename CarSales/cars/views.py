from django.views.generic.list import ListView
from django.views import generic
from django.db.models import Q
from . import choices as ch
from .models import Car
import functools
import operator

class IndexView(ListView):
    model = Car
    paginate_by = 9
    search = False
    template_name = 'index.html' 
    
    # override of get_queryset
    def get_queryset(self):
        #default sorting newest first
        result = Car.objects.all().order_by('-car_year')  
                        
        # Handle sorting input              
        query = self.request.GET.get('sort')            
        if query:   
            self.search = True
            if int(query) == 1:                
                result = result.order_by('car_price')
            elif int(query) == 2:                
                result = result.order_by('-car_price')
            elif int(query) == 3:                
                result = result.order_by('-car_year')
            else:
                result = result.order_by('car_year')
                
        # Handle description input, remove garbage        
        query = self.request.GET.get('desc')                     
        if query:
            self.search = True
            value = ''.join(tok for tok in query if tok.isalnum() or tok == ' ')
            query_list = value.split()
            result = result.filter(functools.reduce(operator.and_, (Q(car_description__icontains = q) for q in query_list)))
            
        # Handle carmake input              
        query = self.request.GET.get('carmake')            
        if query:      
            self.search = True
            result = result.filter(Q(car_make__exact = query))
            
        # Handle carmodel input              
        query = self.request.GET.get('carmodel')            
        if query:  
            self.search = True
            result = result.filter(Q(car_model__exact = query))
            
        # Handle caryear input              
        query = self.request.GET.get('caryear')            
        if query: 
            self.search = True
            result = result.filter(Q(car_year__exact = int(query)))
                                   
        # Handle carprice input              
        query = self.request.GET.get('carprice')            
        if query: 
            self.search = True
            if int(query) == 1:                
                result = result.filter(Q(car_price__lte = 10000))
            elif int(query) == 2:                
                result = result.filter(Q(car_price__range = (10000, 15000)))
            elif int(query) == 3:                
                result = result.filter(Q(car_price__range = (15000, 20000)))
            else:
                result = result.filter(Q(car_price__gte = 20000))
                                       
        # Handle area area input              
        query = self.request.GET.get('area')            
        if query:  
            self.search = True
            result = result.filter(Q(dealer_area__exact = query))
    
        # Handle dealership input              
        query = self.request.GET.get('dealer')            
        if query:
            self.search = True
            result = result.filter(Q(dealer_name__exact = query))
                                
        # return cars
        return result        
        
    # override
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(IndexView, self).get_context_data(**kwargs)                
        
        # add 3 newest picked cars to the context
        context['picked_cars'] = Car.objects.filter(car_picked = True).order_by('-car_year')[:3]
        
        # pass available choices
        context['areas'] = ch.AREA_CHOICES        
        context['makes'] = ch.MAKE_CHOICES
        context['models'] = ch.MODEL_CHOICES        
        context['dealers'] = ch.DEALER_CHOICES    
        context['years'] = Car.objects.all().values_list('car_year').distinct()
        
        # to scrol down page if user has searched
        if self.search:
            context['search'] = True
        else:
            context['search'] = False
        
        return context
            
# class for detail modal
class DetailView(generic.DetailView):
    model = Car
    template_name = 'details.html'
