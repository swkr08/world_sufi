from django.shortcuts import render,HttpResponse,redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone
from django.db.models import Sum
from django.utils.translation import activate
# from .models import UserProfile
from datetime import date
from .models import UserProfile, zikr_count
# Create your views here. 
from django.db import IntegrityError 
from django.http import JsonResponse
from .models import Country, State, City
from django.db.models import Count
# Create your views here.

def index(request):
    context = {
    #    'posts': posts

         'user': User.objects.all(),
        #  'profile': Profile.objects.all()
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html') 

def contact(request):
    return render(request,'contact.html')

def statistics(request):
    return render(request,'statistics.html') 

def forgetpassword(request):
    return render(request, 'forgetpassword.html')

def resetpassword(request):
    return render(request, 'resetpassword.html')
 



def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse({'states': list(states)})

def get_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).values('id', 'name')
    return JsonResponse({'cities': list(cities)})

# def location_selection(request):
#     countries = Country.objects.all()
#     return render(request, 'dashboard.html', {'countries': countries})



@login_required(login_url="/login/")
def dashboard(request):

#    main page
    if request.method =="POST":
        data = request.POST
        form_Zikr_count_id = request.POST.get('form_Zikr_count_id')  # Get the value of the hidden input field
        # print(form_Zikr_count_id)
        if form_Zikr_count_id == 'form_Zikr_count':  # Check if the form ID matches
       
            new_zikr_count = data.get('zikr_count')
            # new_zikr_date = data.get('timezone.now()')
            # rec_image = request.FILES.get('rec_image')
        # print(zikr_count)
    
            user = request.user
            try:
                zikr_count_all=zikr_count.objects.create(user=user, zikr_count = new_zikr_count, zikr_date = timezone.now()) 
                  
            
                return JsonResponse({'zikr_count': new_zikr_count})
                
                # return redirect('/dashboard/')
            except IntegrityError as e:
                print("IntegrityError:", e)
    
    
    today  = timezone.now().date()
    current_day_zikr = zikr_count.objects.filter(user=request.user, zikr_date__date=today).aggregate(Sum('zikr_count'))['zikr_count__sum']
    total_zikr_count = zikr_count.objects.filter(user=request.user).aggregate(Sum('zikr_count'))['zikr_count__sum']
    desired_daily_zikr_count = 1000  # Set your desired daily zikr count here
    # percent_completed = (total_zikr_count / desired_daily_zikr_count) * 100
    all_users_total_zikr = zikr_count.objects.all().aggregate(Sum('zikr_count'))['zikr_count__sum']

    desired_total_zikr = 1000000
    if all_users_total_zikr is not None and desired_total_zikr > 0:
        total_percentage_completed = (all_users_total_zikr / desired_total_zikr) * 100
        rounded_total_percentage_completed = round(total_percentage_completed)
    else:
        rounded_total_percentage_completed = 0
    
    users_with_total_counts = User.objects.annotate(total_zikr_count=Sum('zikr_count__zikr_count'))    
    queryset = zikr_count.objects.filter(user=request.user)
    # print_r(request)
    UserProfile_user = User.objects.get(username=request.user) 
    UserProfile_loc = UserProfile.objects.filter(user_id= request.user.id).first()
    
    # try:
    #     UserProfile = UserProfile.objects.get(user=request.user)
    # except UserProfile.DoesNotExist:
    #     UserProfile = UserProfile(user=request.user)

# location
    countries = Country.objects.all()
  
# group statistics
    # Assuming you have fields like 'country', 'state', and 'city' in UserProfile model
    result = zikr_count.objects.values('user__userprofile__country', 'user__userprofile__state', 'user__userprofile__city').annotate(total_count=Count('zikr_count'))

# Printing the results
    # group_by_country = [item['user__userprofile__country'] for item in result]
    # group_by_state = [item['user__userprofile__state'] for item in result]
    # group_by_city = [item['user__userprofile__city'] for item in result]
    total_count_world = [item['total_count'] for item in result]

    country_each = zikr_count.objects.values('user__userprofile__country').annotate(total_count=Sum('zikr_count'))
    country_total_counts = {}
    for result in country_each:
        country = result['user__userprofile__country']
        total_count = result['total_count']
        country_total_counts[country] = total_count

    state_each = zikr_count.objects.values('user__userprofile__state').annotate(total_count=Sum('zikr_count'))
    state_total_counts = {}
    for result in state_each:
        country = result['user__userprofile__state']
        total_count = result['total_count']
        state_total_counts[country] = total_count
    
    city_each = zikr_count.objects.values('user__userprofile__city').annotate(total_count=Sum('zikr_count'))
    city_total_counts = {}
    for result in city_each:
        country = result['user__userprofile__city']
        total_count = result['total_count']
        city_total_counts[country] = total_count

      #----- search funtion
    all_search = {}
    if request.GET.get('search_rec'):
        search_term = request.GET.get('search_rec')
        
        # Filter the dictionaries based on the search term
        filtered_country_counts = {country: count for country, count in country_total_counts.items() if search_term.lower() in country.lower()}
        filtered_state_counts = {state: count for state, count in state_total_counts.items() if search_term.lower() in state.lower()}
        filtered_city_counts = {city: count for city, count in city_total_counts.items() if search_term.lower() in city.lower()}
        
        # Create a dictionary to store filtered search results
        all_search = {
            'Country': filtered_country_counts,
            'State': filtered_state_counts,
            'City': filtered_city_counts
        }

    # Pass the combined filtered dictionaries to the template
    # context = {
    #     'search_results': all_search
    # }
 
    context = {'zikr_count_get':queryset, 
               'total_zikr_count': total_zikr_count, 
               'current_day_zikr' :current_day_zikr,
            #    'percent_completed':percent_completed,
                'all_users_total_zikr':all_users_total_zikr,
                'rounded_total_percentage_completed': rounded_total_percentage_completed,
                'users_with_total_counts' : users_with_total_counts,
                'countries': countries,
                # 'cities': list(cities),
                # 'states': list(states),
                'UserProfile_user' : UserProfile_user,
                'UserProfile_loc':UserProfile_loc, 
                # 'group_by_country' : group_by_country,
                # 'group_by_state' : group_by_state,
                # 'group_by_city' : group_by_city,
                'total_count_world' : total_count_world,
                'country_total_counts': country_total_counts,
                'state_total_counts': state_total_counts,
                'city_total_counts': city_total_counts,
                'search_results': all_search
                }

    # return JsonResponse(all_search)
    return render(request, 'dashboard.html', context)
    




def login_page(request):
    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username invalid ! Please try some other username.")
            return redirect('/login/')
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.error(request, "password invalid ! Please try some other username.")
            return redirect('/login/')
        
        else:
            login(request, user)
            messages.error(request, "User logged in .")
            return redirect('/dashboard/')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":     
      
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('/register/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('/register/')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('/register/')
        
       
        # myuser = User.objects.create_user(username, email, password)
        # myuser.first_name = fname
        # myuser.last_name = lname
        # myuser.is_active = False
        user = User.objects.create(
            email = email,
            username = username,
        )
        user.set_password(password)
        user.save()
        # myuser.is_active = False
        # myuser.save()
        messages.success(request, "Your Account has been created succesfully!!.")
        
        
        return redirect('/login/')
     
    return render(request, 'register.html')



@login_required(login_url="login")
def edit_profile(request):
    # try:
    #     user_profile = UserProfile.objects.get(user=request.user)
    # except UserProfile.DoesNotExist:
    #     user_profile = UserProfile(user=request.user)
    #     user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form_edit_id = request.POST.get('form_edit_id')  # Get the value of the hidden input field
        if form_edit_id == 'form_edit':  # Check if the form ID matches
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
        
            # Update the attributes of the User instance
            user = request.user
            if email:  # Only update if email is provided
                user.email = email
                user.save()

            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            # Update the attributes of the user_profile instance
            if not request.POST.get('country').isnumeric():
                pass
            else:
                country = request.POST.get('country')
                country_name = Country.objects.filter(id=country).first()
                user_profile.country = country_name.name
            
             
            if not request.POST.get('state').isnumeric():
                pass
            else:
                state = request.POST.get('state')
                state_name = State.objects.filter(id=state).first()
                user_profile.state = state_name.name

            if not request.POST.get('city').isnumeric():
                pass
            else:
                city = request.POST.get('city')
                city_name = City.objects.filter(id=city).first()
                user_profile.city = city_name.name
            
            # user_profile.country = country_name.name
            # user_profile.state = state_name.name
            # user_profile.city = city_name.name
                user_profile.phone = phone
                user_profile.email = email
                user_profile.save()


            # Update user email if provided
            if email and email != request.user.email:
                request.user.email = email
                request.user.save()
            #  return redirect('/dashboard/')
            # response_data = {'user_profile': user_profile}
            # return JsonResponse(response_data)
            return redirect('/dashboard/')

        context = {
            'user_profile': user_profile,
            
        }
    # user_profile = user_profile.objects.get(user=user_profile)
    return render(request, 'dashboard.html', context)


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/login/')






