from django.db import models

class MainPage(models.Model):
    company_img = models.ImageField(upload_to='media/images', null=True)
    aboutCompany = models.CharField(max_length=150)
    history = models.CharField(max_length=150)
    founder = models.CharField(max_length=150)
    founded_year = models.CharField(max_length=150)
    location = models.CharField(max_length=150)

class Employees(models.Model):
    photo = models.ImageField(upload_to='media/images', null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    