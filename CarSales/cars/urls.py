from django_filters.views import FilterView
from django.urls import path
from .models import Car
from . import views

app_name = 'cars'

# to prefix the urls
urlpatterns = [    
    # ex: /cars/
    path('', views.IndexView.as_view(), name = 'index'),                   
    
    # ex: /cars/5/
    path('<int:pk>/', views.DetailView.as_view(), name = 'details'), 
]
