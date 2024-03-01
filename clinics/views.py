from contextlib import _RedirectStream
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate ,login,logout
from .forms import UserRigister, contactus 

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def SignUp(request):

    if request.method == 'POST':
        form=UserRigister(request.POST)
        if form.is_valid():
            form.save()
        redirect('signin')
        
    elif request.method == 'GET':
        form =UserRigister()
        context={'form': form}
        return render(request, 'SignUp.html', context)
    template = loader.get_template('SignUp.html')
    return HttpResponse(template.render())

def SignIn(request):
    template = loader.get_template('SignIn.html')
    if request.method == 'POST':
       phone=request.POST['phone'] 
       password=request.POST['password']
       user=authenticate(request,phone=phone,password=password)
       if user is not None:
           login(request,user)
       else:
           return redirect('/signin')


    else:
         return HttpResponse(template.render())

def home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())

def ContactUs(request):
    if request.method == 'POST':
        form=contactus(request.POST)
        if form.is_valid():
            form.save()
        redirect('homepage')
    template = loader.get_template('ContactUs.html')
    return HttpResponse(template.render())

def AboutUs(request):
    template = loader.get_template('AboutUs.html')
    return HttpResponse(template.render())
