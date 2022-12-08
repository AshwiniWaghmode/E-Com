from django.contrib import admin
from django.urls import path
from Shop import views

urlpatterns = [
    path('', views.index,name="index"),
    path('register', views.register,name="register"),
    path('login',views.login,name="login"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('category',views.category,name="category"),
    path('popup',views.popup,name="popup"),
    path('v_home',views.v_home,name="v_home"),
    path('art',views.art,name="art"),
    path('craft',views.craft,name="craft")
]