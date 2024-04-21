from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=64, blank=True)
    isLost = models.BooleanField(default=True)
    specie = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='animal_photos/', blank=True)
    date = models.DateTimeField(auto_now=True)
    
