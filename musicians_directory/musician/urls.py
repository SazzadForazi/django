from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.add_musician,name='add_musician' ),
]