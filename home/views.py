import email
import cv2
from PIL import Image
import numpy as np
from numbers import Rational
import re
import io

import os
from django.shortcuts import get_object_or_404, render , HttpResponse , redirect , get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import postss ,messagess, profiles, reviews
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
import os

import cv2
class Cartoonizer:
 """Cartoonizer effect
  A class that applies a cartoon effect to an image.
  The class uses a bilateral filter and adaptive thresholding to create
  a cartoon effect.
 """
 def __init__(self):
  pass

 def render(self, img_rgb):
  img_rgb = cv2.imread(img_rgb)
  img_rgb = cv2.resize(img_rgb, (1366,768))
  numDownSamples = 2  # number of downscaling steps
  numBilateralFilters = 50 # number of bilateral filtering steps

  # -- STEP 1 --

  # downsample image using Gaussian pyramid
  img_color = img_rgb
  for _ in range(numDownSamples):
   img_color = cv2.pyrDown(img_color)

  #cv2.imshow("downcolor",img_color)
  #cv2.waitKey(0)
  # repeatedly apply small bilateral filter instead of applying
  # one large filter
  for _ in range(numBilateralFilters):
   img_color = cv2.bilateralFilter(img_color, 9, 9, 7)

  #cv2.imshow("bilateral filter",img_color)
  #cv2.waitKey(0)
  # upsample image to original size
  for _ in range(numDownSamples):
   img_color = cv2.pyrUp(img_color)
  #cv2.imshow("upscaling",img_color)
  #cv2.waitKey(0)

  # -- STEPS 2 and 3 --
  # convert to grayscale and apply median blur
  img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
  img_blur = cv2.medianBlur(img_gray, 3)
  #cv2.imshow("grayscale+median blur",img_color)
  #cv2.waitKey(0)

  # -- STEP 4 --
  # detect and enhance edges
  img_edge = cv2.adaptiveThreshold(img_blur, 255,
          cv2.ADAPTIVE_THRESH_MEAN_C,
          cv2.THRESH_BINARY, 9, 2)
  #cv2.imshow("edge",img_edge)
  #cv2.waitKey(0)

  # -- STEP 5 --
  # convert back to color so that it can be bit-ANDed with color image
  (x,y,z) = img_color.shape
  img_edge = cv2.resize(img_edge,(y,x))
  img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
  cv2.imwrite("edge.png",img_edge)
  #cv2.imshow("step 5", img_edge)
  #cv2.waitKey(0)
  #img_edge = cv2.resize(img_edge,(i for i in img_color.shape[:2]))
  #print img_edge.shape, img_color.shape
  return cv2.bitwise_and(img_color, img_edge)


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
    
    return render(request ,'index_old.html',context)
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

        fs = FileSystemStorage() 
        
        na = pr.image.name
        print(na)
        path = './static/images/'+na
        print(img)
        cart = Cartoonizer()
        im =cart.render(path)
        im= cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
        P = Image.fromarray(im)
        p_io = io.BytesIO()
        P.save(p_io , format='JPEG')
        p_file  = InMemoryUploadedFile(p_io,None , 'yiy.jpg','image/jpeg',None,None)
        pr.delete()
        pr = postss(name =nam , number =passwor , image = p_file ,host = request.user)
        pr.save()

        P.show()
        


    return render(request , 'contact.html')

def firs(request):
    return render(request , 'first.html')