from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from post.models import Post
# Create your views here.
# @login_required
# def index(request):
#     return render(request,'index.html')

class HomeView(ListView):
    model = Post
    template_name= 'index.html'
    context_object_name='posts'