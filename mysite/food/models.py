from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
##Models:- A blueprint to create database tables these models define how the table contents are....

class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image  = models.CharField(max_length=500,default="https://imgs.search.brave.com/Qew1jLRC8BCdLELrrPbZ6MW0SAv5reqcRh0pIhojvcM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA4LzI2Lzc3LzI5/LzM2MF9GXzgyNjc3/Mjk1NF9IcU9pMVRJ/cUVwbkZjbXJsR1Qx/QWxSRHo5RVd4M0tk/cS5qcGc")
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    