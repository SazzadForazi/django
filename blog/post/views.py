from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from post.forms import PostForm
# Create your views here.
class CreatePostView(CreateView):
    template_name='createPost.html'
    form_class = PostForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
      form.instance.author = self.request.user
      messages.success(self.request, "Post created successfully")
      return super().form_valid(form)
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['title'] = 'Create a Post'
       context['button'] = 'Create'
       return context