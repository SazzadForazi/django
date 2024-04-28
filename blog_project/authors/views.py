from django.shortcuts import render

# Create your views here.
def add_authors(request):
    return render(request,'add_authors.html')