from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def add_catagory(request):
    if request.method == 'POST': # if user click submit button
        category_form = forms.CategoryForm(request.POST) 
        if category_form.is_valid():
            category_form.save()
            return redirect('add_catagories') 
    
    else: # user normally website e gele blank form pabe
        category_form = forms.CategoryForm()
    return render(request, 'add_catagory.html', {'form' : category_form})