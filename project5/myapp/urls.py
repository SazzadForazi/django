from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about,name="about"),
    path('form/',views.submit_form, name="submit_form"),
    path('django_forms/',views.Django_forms, name='django_forms' )
]