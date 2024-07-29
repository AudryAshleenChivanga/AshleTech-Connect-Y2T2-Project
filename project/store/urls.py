from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('articles/', views.article_list, name="article_list"),
    path('articles/<int:article_id>/', views.article_detail, name="article_detail"),
    path('specialists/', views.specialist_list, name="specialist_list"),
    path('specialists/<int:specialist_id>/', views.specialist_detail, name="specialist_detail"),
]
