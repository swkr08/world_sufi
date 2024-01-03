 
>>> from malaysia_app.models import UserProfile 
>>> user = UserProfile.objects.get              
>>> user
<bound method QuerySet.get of <django.db.models.manager.Manager object at 0x000001F12CCC8150>>
>>> user.name
 
>>> user(country='india', state='karnataka', city='bangalore', email='y@mail.com',phone=5678)
 
>>> user(country='india', state='karnataka', city='bangalore', email='y@mail.com',phone=5678)
 
>>> user(country='india', state='karnataka', city='bangalore', email='y@mail.com',phone=5678)
 >>> user = UserProfile.objects.all()                                      
>>> user.country
>>> new_user = UserProfile(country='india', state='karnataka', city='bangalore', email='y@mail.com', phone=5678)
>>> new_user = UserProfile(country='india', state='karnataka', city='bangalore', email='y@mail.com', phone=5678)
>>> new_user.save()
>>> user = UserProfile.objects.all()                                      
>>> UserProfile.username
  
>>> UserProfile         
<class 'malaysia_app.models.UserProfile'>
 
 >>> from malaysia_app.models import Country,State, City 
>>> from malaysia_app.models import Country, State, City 
 >>> from malaysia_app.models import Country             
 
>>> from malaysia_app.models import Country, State, City 
>>> Country.objects.all()   
>>> Country.objects.all()   
>>> Country.objects.all()
<QuerySet [<Country: Afghanistan>, <Country: Aland Islands>, <Country: Albania>, <Country: Algeria>, <Country: American Samoa>, <Country: Andorra>, <Country: Angola>, <Country: Anguilla>, <Country: Antarctica>, <Country: Antigua And Barbuda>, <Country: Argentina>, <Country: Armenia>, <Country: Aruba>, <Country: Australia>, <Country: Austria>, <Country: Azerbaijan>, <Country: Bahrain>, <Country: Bangladesh>, <Country: Barbados>, <Country: Belarus>, '...(remaining elements truncated)...']>
>>> from malaysia_app.models import UserProfile   
>>> UserProfile.objects.all()
 
>>> from malaysia_app.models import UserProfile                           
>>> user = UserProfile.objects.all()                                      
>>> UserProfile.objects.all()        
<QuerySet [<UserProfile: Profile for user with ID 1>, <UserProfile: younus_geen>]>
>>> UserProfile.objects.get(user=request.user) 
 
>>> UserProfile.objects.get(user='younus')  
>>> UserProfile.objects.get(user='y')  
>>> UserProfile.objects.get(user='1') 

>>> UserProfile.objects.get(user=2) 
<UserProfile: younus_geen>
>>> UserProfile.objects.get(user)  

>>> UserProfile.objects.all(user)  
>>> u = UserProfile.objects.all()  
>>> u
<QuerySet [<UserProfile: Profile for user with ID 1>, <UserProfile: younus_geen>]>
>>> UserProfile.objects.filter(user=2)     
<QuerySet [<UserProfile: younus_geen>]>
>>> UserProfile.objects.filter(user=request.id) 
 
>>> from django.shortcuts import render,HttpResponse,redirect
>>> UserProfile.objects.filter(user=request.id)

>>> u = UserProfile.objects.filter(user_id=2).first()

>>> u.country
'indian'
>>> c = Country.objects.filter(country=15).first()   

>>> from malaysia_app.models import Country, State, City
>>> c = Country.objects.filter(country=15).first() 
>>> c = Country.objects.filter(id=15).first()        
>>> c 
<Country: Austria>
>>> c.name
'Austria'

>>> s = State.objects.filter(id=2057).first()
>>> s.name
'Carinthia'


>>> un=User.objects.filter(username='younusgeen').first()
>>> un=User.objects.get(username='younus_geen')
>>> un.id
2
>>> u = UserProfile.objects.filter(user_id=un.id).first()
>>> u.country
'Australia'
>>> cc = [item['user__userprofile__country'] for item in result] 
 
>>> from malaysia_app.models import zikr_count                            
>>> result = zikr_count.objects.values('user__userprofile__country', 'user__userprofile__state', 'user__userprofile__city') \.annotate(total_count=Count('zikr_count'))
  File "<console>", line 1
    result = zikr_count.objects.values('user__userprofile__country', 'user__userprofile__state', 'user__userprofile__city') \.annotate(total_count=Count('zikr_count'))
       
>>> result = zikr_count.objects.values('user__userprofile__country', 'user__userprofile__state', 'user__userprofile__city').annotate(total_count=Count('zikr_count'))   
 
>>> from django.db.models import Count                                    
>>> result = zikr_count.objects.values('user__userprofile__country', 'user__userprofile__state', 'user__userprofile__city').annotate(total_count=Count('zikr_count'))
>>> gc =  group_by_country = [item['user__userprofile__country'] for item in result]
>>> gc
['Australia']
>>> gc.total_count 
 
>>> tc = [item['total_count'] for item in result]                     
>>> tc
[5]
 
>>> result = zikr_count.objects.values('user__userprofile__country').annotate(total_count=Sum('zikr_count')) 
>>> group_by_country = [item['user__userprofile__country'] for item in result]
>>> total_count_by_country = [item['total_count'] for item in result]
>>> total_count_by_country                                           
[112]
 
>>> group_by_country           
['Australia']
from django.db.models import Sum

