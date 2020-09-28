from django.db import models

# Create your models here.


class Admin(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.username


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mobile_number = models.IntegerField(max_length=11)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category)
    price = models.IntegerField(max_length=20)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=20)
    ratings = models.IntegerField(max_length=20)
    quantity = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Order(models.Model):
    order_name = models.IntegerField(max_length=20)
    product_id = models.ForeignKey(Product)
    customer_id = models.ForeignKey(Customer)
    delivered = models.CharField(max_length=20)
    order_number = models.IntegerField()
    paid = models.CharField(max_length=20)
    payment_id = models.ForeignKey(Payment)

    def __str__(self):
        return self.order_name


class Payment(models.Model):
    card_number = models.IntegerField(max_length=20)
    csv = models.CharField(max_length=20)
    expiry_month = models.IntegerField(max_length=10)
    expiry_year = models.IntegerField(max_lenghth=10)
    customer_id = models.ForeignKey(Customer)
    card_type = models.CharField(max_length=20)

    def __str__(self):
        return self.card_number



