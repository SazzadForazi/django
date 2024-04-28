from django.shortcuts import render

# Create your views here.
def add_profiles(request):
    return render(request,'add_profiles.html')