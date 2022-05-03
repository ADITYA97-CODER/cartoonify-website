
from pyexpat import model
from django.db import models

# Create your models here.
from django.db import models
import os
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class messagess(models.Model):
    mess= models.CharField(max_length=100)
    sender = models.ForeignKey(User , on_delete=CASCADE, default=None)
    recievers =models.ForeignKey(User , related_name= 'reciever',on_delete=CASCADE , default=None ,null=True)


    
# Create your models here.
class postss(models.Model):
    host = models.ForeignKey(User , on_delete=models.CASCADE ,null=True)
    name = models.CharField(max_length=122)
    number = models.CharField(max_length=122)
    image = models.ImageField( upload_to= 'images/' ,null=True , blank=True)
    
class profiles(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, primary_key= True, default=None)  
    names = models.CharField(max_length=211, null=True,default='none')
    pic = models.ImageField(upload_to = 'images/',null= True , blank = True)
    bio = models.CharField(max_length=200 ,null=True)


class reviews(models.Model):
    person_reviewed = models.ForeignKey(User ,on_delete=models.CASCADE , null=True)
    users = models.ForeignKey(User , related_name= 'reviewer',on_delete=CASCADE , default=None ,null=True)
    content = models.CharField(max_length=300)
    rating = models.IntegerField()
