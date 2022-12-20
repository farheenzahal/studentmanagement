from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.mainhome,name="mainhome"),

    path('contact/', views.contact,name="contact"),
    path('sign', views.sign,name="sign"),
    path('signup/', views.signup,name="signup"),
    path('forgot/', views.forgot,name="forgot"),
    path('gallery/', views.gallery,name="gallery"),
    path('course/', views.course,name="course"),


]