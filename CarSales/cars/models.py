from sorl.thumbnail import ImageField
from django.db import models
from . import choices as ch

# model to store different cars
class Car(models.Model):    
    # car info        
       
    car_year = models.IntegerField('Year')
    car_image = ImageField('Image', upload_to = 'cars/')  
    car_web = models.URLField('Website', max_length = 200)    
    car_picked = models.BooleanField('Is Picked',default = False)    
    car_price = models.DecimalField('Price', max_digits = 8, decimal_places = 2)
    car_make = models.CharField('Make', max_length = 200, choices = ch.MAKE_CHOICES)    
    car_model = models.CharField('Model', max_length = 200, choices = ch.MODEL_CHOICES) 
                 
    
    #dealer info    
    dealer_name = models.CharField('Dealership', max_length = 200, choices = ch.DEALER_CHOICES)
    dealer_zip = models.IntegerField('Area Zip', choices = ch.ZIP_CHOICES)
    dealer_web = models.URLField('Dealer Website', max_length = 200)            
    # other info ...
    