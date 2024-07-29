from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress, Article, Specialist

# Customize the admin site
admin.site.site_header = "AshleTech Connect SRHR Admin"
admin.site.site_title = "AshleTech Connect SRHR Admin Portal"
admin.site.index_title = "Welcome to AshleTech Connect SRHR Admin Portal"

# Custom admin forms
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('published_date',)

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'field', 'contact_info', 'picture')
    search_fields = ('name', 'field')
    list_filter = ('field',)

# Registering my models here
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Specialist, SpecialistAdmin)
