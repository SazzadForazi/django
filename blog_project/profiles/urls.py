from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.add_profiles,name='add_profiles' ),
]