from django.shortcuts import render

def about(request, id):
    return render(request, 'url.html', {'id': id})

def index(request):
    id = None  # Or you can set it to any default value
    return render(request, 'url.html', {'id': id})
