from django.contrib import admin
from .models import *
# Register your models here.
# from app.models import Contact
from .models import Country,State, City
# Register your models here.
admin.site.register(Country)

admin.site.register(State)

admin.site.register(City)

admin.site.register(zikr_count)

admin.site.register(UserProfile)

# admin.site.register(Contact)