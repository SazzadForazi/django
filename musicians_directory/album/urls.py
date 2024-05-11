from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.add_album,name='add_album' ),
]