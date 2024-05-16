from django.urls import path
from post.views import CreatePostView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    
]