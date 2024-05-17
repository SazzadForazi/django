from django.urls import path
from post.views import CreatePostView,PostDetailView,UpdatePostView

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('detail/<str:slug>',PostDetailView.as_view(),name='detail-post'),
    path('update/<str:slug>', UpdatePostView.as_view(), name='update-post'),
]