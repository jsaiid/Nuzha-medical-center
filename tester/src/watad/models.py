from django.db import models
from django import forms



# Create your models here.

class activities(models.Model):
    id=models.AutoField(primary_key=True,) 
    image=models.FileField(upload_to="media/activites", default="")
    title =models.CharField(max_length=100 , default="")
    desc =models.TextField(max_length=100 , default="")
    date = models.DateTimeField()


class partners(models.Model):
    id=models.AutoField(primary_key=True,) 
    image=models.FileField(upload_to="media/partners", default="")
    name =models.CharField(max_length=100 , default="")


class activity(models.Model):
    id=models.AutoField(primary_key=True,) 
    name =models.CharField(max_length=100 , default="")
    date = models.DateTimeField()
    exp_date = models.DateTimeField()
    email=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    about_watad=models.TextField(max_length=100 , default="")
    proj_title=models.TextField(max_length=100 , default="")
    desc =models.TextField(max_length=100 , default="")
    training_prog=models.TextField(max_length=100 , default="")
    proj_length=models.TextField(max_length=100 , default="")
    quotation_currency=models.TextField(max_length=100 , default="")
    how_to_apply=models.TextField(max_length=100 , default="")
    note=models.TextField(max_length=100 , default="")



class contact(models.Model):
    id=models.AutoField(primary_key=True,) 
    name =models.CharField(max_length=100 , default="")
    email=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    subject =models.TextField(max_length=100 , default="")
    message=models.CharField(max_length=200,default="")


class details_job (models.Model):
    id=models.AutoField(primary_key=True,) 
    image=models.FileField(upload_to="media/job", default="")
    title=models.CharField(max_length=100 , default="")
    desc =models.TextField(max_length=100 , default="")
    date = models.DateTimeField()



class calls(models.Model):
    id=models.AutoField(primary_key=True,) 
    name =models.CharField(max_length=100 , default="")
    date = models.DateTimeField()
    exp_date = models.DateTimeField()
    email=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    mobile=models.CharField(max_length=200,default="")
    subject =models.TextField(max_length=100 , default="")



    




    

