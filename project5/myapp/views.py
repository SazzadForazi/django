from django.shortcuts import render
from .forms import contactForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
       # print(request.POST)
    if request.method =='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,'about.html',{'name':name, 'email':email, 'select':select})
    return render(request,'about.html')

def submit_form(request):
    return render(request,'form.html')




#View Function for contactForm Form-Class
def Django_forms(request):
    form = contactForm(request.POST)
    # print(request.POST)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request,"django_forms.html",{'form':form})