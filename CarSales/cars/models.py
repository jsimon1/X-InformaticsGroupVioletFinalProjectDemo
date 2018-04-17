from sorl.thumbnail import ImageField
from django.db import models

# model to store different cars
class Car(models.Model):
    
    # car info        
    car_image = ImageField(upload_to = 'cars')  
    car_web = models.URLField(max_length = 200)
    car_year = models.IntegerField('Model Year')
    car_make = models.CharField(max_length = 200)    
    car_model = models.CharField(max_length = 200)    
    car_picked = models.BooleanField(default = False)
    car_price = models.DecimalField(max_digits = 8, decimal_places = 2)     
    
    #dealer info    
    dealer_name = models.CharField(max_length = 200)
    dealer_web = models.URLField(max_length = 200)
    dealer_zip = models.IntegerField(default=0)
        
    # other info ...