from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

from django.core.management.base import BaseCommand
import pdb

class MyCommand(BaseCommand):
    def handle(self, *args, **options):
        # Insert this line to start the debugger
        pdb.set_trace()

        # Your command logic here

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True )
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        if self.user:
            return self.user.username
        return f"Profile for user with ID {self.pk}"

# Create your models here.
class zikr_count(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
    # zikr_name = models.CharField(max_length=50)
    zikr_count = models.IntegerField()
    zikr_date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return f"{self.user.username}'s Zikr Count"
    
    # def __str__(self):
    #     return self.name


# Create your models here.
class Country(models.Model):
    name = models.TextField()
    iso3 = models.TextField()
    iso2 = models.TextField()
    numeric_code = models.IntegerField()
    phone_code = models.TextField()
    capital = models.TextField()
    currency = models.TextField()
    currency_name = models.TextField()
    currency_symbol = models.TextField()
    tld = models.TextField()
    native = models.TextField()
    region = models.TextField()
    subregion = models.TextField()
    nationality = models.TextField()
    timezones = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    emoji = models.TextField()
    emojiU = models.TextField()

    def __str__(self):
        return self.name
    


class State(models.Model):
    name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    country_code = models.TextField()
    country_name = models.TextField()
    state_code = models.TextField()
    type = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

from django.db import models

class City(models.Model):
    name = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    state_code = models.TextField()
    state_name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    country_code = models.TextField()
    country_name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    wikiDataId = models.TextField()

    def __str__(self):
        return self.name
