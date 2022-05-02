from email import message
from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.firs,name='login'),
    path("login",views.loginpage,name='login'),
    path("register",views.registeruser,name='register'),
    path("logout",views.logoutuser,name='logout'),
    path("contact",views.contact,name='contact'),
    path('profile/<str:pk>/', views.userprofile , name ='user-profile'),
    #path('profile', views.pro, name ='profile'),
    path('messages/<str:pk>/' , views.mes , name = 'message'),
    
    path('profile/<str:pk>/addreview/',views.create_review, name= 'create_review'),
    path('home',views.index,name='home'),


    
]
