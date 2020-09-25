from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mobile_number = models.IntegerField(max_length=11)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)