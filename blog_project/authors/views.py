
from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def add_author(request):
    
    author_form = forms.AuthorForm()
    return render(request, 'add_authors.html', {'form' : author_form})