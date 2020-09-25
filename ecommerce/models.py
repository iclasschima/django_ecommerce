from django.db import models

# Create your models here.


class Admin(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mobile_number = models.IntegerField(max_length=11)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


<<<<<<< HEAD
class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category)
    price = models.IntegerField(max_length=20)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=20)
    ratings = models.IntegerField(max_length=20)
    quantity = models.IntegerField()
=======
class Category(models.Model):
    caterory_name = models.CharField(max_length=100)
>>>>>>> ff74079737f1c4bb3fe96d4aa131a10b910a335e
