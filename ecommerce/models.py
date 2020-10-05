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
    mobile_number = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=20)
    ratings = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    card_number = models.IntegerField()
    csv_number = models.CharField(max_length=20)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=20)

    def __str__(self):
        return self.card_number


class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivered = models.CharField(max_length=20)
    order_number = models.IntegerField()
    paid = models.CharField(max_length=20)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_name
