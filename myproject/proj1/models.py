from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse

class Categary(models.Model):
    Id = models.IntegerField(max_length=20)
    Name = models.CharField(max_length=128)
    Image = models.ImageField(upload_to='Images/', null=True, blank=True)

    def __str__ (self):
        return self.Name

    def delete(self, *args, **kwargs):
        self.Image.delete()
        super().delete(*args, **kwargs)

class subcategary(models.Model):
    Id = models.IntegerField(max_length=20)
    categary = models.ForeignKey(Categary,on_delete=models.CASCADE)
    Name = models.CharField(max_length=128)
    Image = models.ImageField(upload_to='Images/', null=True, blank=True)

    def __str__ (self):
        return self.Name

class Brand(models.Model):
    Id = models.IntegerField(max_length=20)
    Name = models.CharField(max_length=128)
    Image = models.ImageField(upload_to='Images/brands/', null=True, blank=True)

    def __str__ (self):
        return self.Name

class catalog(models.Model):
    Id = models.IntegerField(max_length=20)
    Brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    Name = models.CharField(max_length=128)
    Image = models.ImageField(upload_to='Images/catalog/', null=True, blank=True)

    def __str__ (self):
        return self.Name

class product(models.Model):
    Id = models.IntegerField(max_length=20)
    Name = models.CharField(max_length=128)
    Image = models.ImageField(upload_to='Images/catalog/', null=True, blank=True)
    Price = models.IntegerField(max_length=128)
    Size = models.IntegerField(max_length=128)
    Quality =models.CharField(max_length=128)
    Requirement = models.IntegerField(max_length=128)
    Tag = models.CharField(max_length=128)
    offer = models.IntegerField(max_length=128)

    def __str__ (self):
        return self.Name
