from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.add_posts,name='add_posts' ),
]