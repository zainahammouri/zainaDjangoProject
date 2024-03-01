from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('indexpage',index,name='indexpage'), 
  path('signup/',SignUp,name='signup'),
  path('signin/',SignIn,name='signin'),
  path('homepage',home,name='homepage'),
  path('contactus',ContactUs,name='contactus'),
  path('aboutus',AboutUs,name='aboutus'),
]