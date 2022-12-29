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
    path('craft',views.craft,name="craft"),
    path('earring',views.earring,name="earring"),
    path('necklace',views.necklace,name="necklace"),
    path('otherj',views.otherj,name="other_jwellary"),
    path('vendor_regi',views.vendorregi,name="vendor_regi"),
    path('painting',views.painting,name="painting"),
    path('plates',views.plates,name="plates"),
    path('bowls',views.bowls,name="bowls"),
    path('wooden',views.wooden,name="wooden"),
    path('other',views.other,name="other"),
    path('custhome',views.custhome,name="custhome"),
    path('v_faq',views.faq,name="faq"),
    path('other',views.other,name="other_homedecor")
]