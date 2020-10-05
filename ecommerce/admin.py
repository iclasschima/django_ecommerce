from django.contrib import admin

# Register your models here.

from .models import Product, Category, Admin, Payment, Customer, Order

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(Admin)
admin.site.register(Order)
admin.site.register(Customer)
