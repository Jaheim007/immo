from email.mime import image
from xml.parsers.expat import model
from django.db import models

class SiteInfo(models.Model):
    section_about_title = models.CharField(max_length=255)
    section_choose_title = models.CharField(max_length=255)
    section_services_title = models.CharField(max_length=255)
    section_project_title = models.CharField(max_length=255)
    section_members_title = models.CharField(max_length=255)
    section_appointment_title = models.CharField(max_length=255)
    logo = models.ImageField()

class Services(models.Model):
    libele = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField(max_length =500)

class Banners(models.Model):
    image = models.ImageField()
    libele = models.CharField(max_length =255) 
    description = models.TextField(max_length =255)

class Manage(models.Model):
    libele  = models.CharField(max_length =255)
    description = models.TextField(max_length =500)
    image = models.ImageField()

class About(models.Model):
    description = models.TextField(max_length= 500)
    experience = models.IntegerField()
    image = models.ImageField()

class Choose(models.Model):
    title =  models.CharField(max_length=255)
    libele = models.CharField(max_length =255) 
    work = models.ForeignKey(Manage, on_delete=models.CASCADE)

# Create your models here.
