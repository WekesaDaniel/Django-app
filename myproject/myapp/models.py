from django.db import models

# Create your models here.

# models.py
from django.db import models

class UserDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    post_office_box = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

# jewelry database model

class Item(models.Model):
    image = models.ImageField(upload_to='images')
    type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    occasion = models.CharField(max_length=100)
    other_details = models.TextField()

    def __str__(self):
        return self.type

