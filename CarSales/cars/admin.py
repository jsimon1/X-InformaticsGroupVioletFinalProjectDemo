from django.contrib import admin
from .models import Car

# register car objects to be modifiable by admin
admin.site.register(Car)
