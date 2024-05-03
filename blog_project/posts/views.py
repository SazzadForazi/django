from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_posts(request):
    if request.method == 'POST': # user post request koreche
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    
    else: # user normally website e gele blank form pabe
        post_form = forms.PostForm()
    return render(request, 'add_posts.html', {'form' : post_form})

def edit_posts(request,id):
        post = models.Post.objects.get(pk=id)
        edit_form = forms.PostForm(instance=post)
        if request.method == 'POST': # user post request koreche
            edit_form = forms.PostForm(request.POST,instance=post)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('homepage')
    
        return render(request, 'add_posts.html', {'form' : edit_form})
    
def delete_posts(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')