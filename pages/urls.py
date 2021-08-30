from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name="index"),
    path('products/gym', views.gym, name="products/gym"),
    path('products/electronics', views.electronics, name="products/electronics"),
    path('products/kitchen', views.kitchen, name="products/kitchen"),
    path('products/clothing', views.clothing, name="products/clothing"),
    path('products/shoes', views.shoes, name="products/shoes"),
    path('products/everyday_things', views.everyday_things, name="products/everyday_things"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
]
