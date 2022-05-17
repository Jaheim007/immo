from xml.parsers.expat import model
from django.db import models
from django.forms import EmailField

class Contact(models.Model):
    nom  = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=255)  
    choose_service = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(max_length=500)

class new(models.Model):
    email = models.EmailField(max_length=254)

class testimonial(models.Model):
    image = models.ImageField()
    description = models.TextField(max_length=500)
    nom  = models.CharField(max_length=255)
    metier = models.CharField(max_length=255)

class Members(models.Model):
    nom = models.CharField(max_length=255) 
    metier = models.CharField(max_length=255)
    image = models.ImageField()

class reseau(models.Model):
    location = models.URLField()
    dial_code = models.CharField(max_length=4) 
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    fb_link = models.URLField()
    insta_link = models.URLField()
    twitter_link = models.URLField()    

# Create your models here.
