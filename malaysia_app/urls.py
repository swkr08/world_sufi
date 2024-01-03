from django.contrib import admin
from django.urls import path,include
from malaysia_app import views
urlpatterns = [
    path('',views.index,name='m-home'),
    path('contact/',views.contact,name='m-contact'),
    path('statistics/',views.statistics,name='m-statistics'),
    path('about/',views.about,name='m-about'),
    path('dashboard/',views.dashboard,name='m-dashboard'),
    path('login/',views.login_page,name='m-login'),
    path('register/',views.register,name='m-register'),
    path('forgetpassword/',views.forgetpassword,name='m-forget'),
    path('resetpassword/',views.resetpassword,name='m-reset'),
    
    # path('csc',views.csc,name='csc'),
    path('get_states/', views.get_states, name='get_states'),
    path('get_cities/', views.get_cities, name='get_cities'),

    path('logout/', views.signout, name='signout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

]