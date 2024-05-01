from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.add_catagory,name='add_catagory' ),
]