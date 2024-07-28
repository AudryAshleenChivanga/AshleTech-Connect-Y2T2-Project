from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress

# Customize the admin site
admin.site.site_header = "AshleTech Connect SRHR Admin"
admin.site.site_title = "AshleTech Connect SRHR Admin Portal"
admin.site.index_title = "Welcome to AshleTech Connect SRHR Admin Portal"

# Register your models here
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
