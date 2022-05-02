import email
from numbers import Rational
import re
from django.shortcuts import get_object_or_404, render , HttpResponse , redirect , get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import postss ,messagess, profiles, reviews
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import os
def loginpage(request):
    page = 'login'
    if request.method =='POST':
        username= request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
          user = user.objects.get(username=username)
        except:
            messages.error(request , 'user does not exist')
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request  , user)
            return redirect('home')    
    context = {'page': page}
    return render(request ,'login.html',context)
# Create your views here.
def logoutuser(request):
    logout(request)
    return redirect('login')

def registeruser(request):
    page = 'register'
    form =  UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username  = user.username.lower()
            user.save()
            login(request , user)
            return redirect('home')


    context = {'form':form}
    return render(request , 'login.html' , context)
@login_required(login_url='/login')
def index(request):
    host = request.user
    item = postss.objects.all()
    profile = profiles.objects.all()
    context = { 'items':item , 'profiles':profile , 'host':host}
    
    return render(request ,'index.html',context)
@login_required(login_url='/login')
def mes(request , pk):
    user = User.objects.get(id = pk)
    meso = messagess.objects.filter(recievers=user)
    if meso :
        m = 'yes'
    else:
        m='no'    
    context = {'messages':meso,'m':m}
    return render(request , 'blank.html' , context)
def create_review(request , pk):
     user = User.objects.get(id=pk)
     create = 'yes'
     host = request.user
     if request.method == 'POST':
        revie = request.POST.get('review')
        rrating = request.POST.get('rating')
        person_reviewe = user
        reviewer= request.user

        reviwed = reviews(person_reviewed = person_reviewe , users = reviewer , content = revie, rating =rrating)
        reviwed.save()
     review = reviews.objects.filter(person_reviewed=user)
     context = {'user':user,'reviews':review , 'create':create ,'host':host}

     return render(request , 'profile.html',context ) 
def userprofile(request,pk ):
     host = request.user
     user = User.objects.get(id=pk)
     if request.method == 'POST':
        revie = request.POST.get('review')
        rrating = request.POST.get('rating')
        person_reviewe = user
        reviewer= request.user

        reviwed = reviews(person_reviewed = person_reviewe , users = reviewer , content = revie, rating =rrating)
        reviwed.save()
     review = reviews.objects.filter(person_reviewed=user)
     context = {'user':user,'reviews':review ,'host':host}

     return render(request , 'profile.html',context )    
def contact(request ):
    if request.method == "POST":
        print(request.user)
        nam = request.POST.get('name')
        passwor = request.POST.get('number')
        img = request.FILES['image']
        pr = postss(name = nam , number = passwor , image = img , host = request.user)
        pr.save()     

    return render(request , 'contact.html')

    