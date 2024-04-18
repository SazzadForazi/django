from django.shortcuts import render

# Create your views here.
def about(request,id):
    return render(request, 'url.html',{'id':id})


def index(request):
    return render(request,'url.html')