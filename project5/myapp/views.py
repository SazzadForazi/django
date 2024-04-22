from django.shortcuts import render
from . forms import contactForm,StudentData,PasswordValidationForm
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
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./myapp/uploads/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request,"django_forms.html",{'form':form})




# New Code , for StuentData Form-Class
def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, "django_forms.html", {'form':form})


#matching password

def my_view(request):
    if request.method =='POST':
        form = PasswordValidationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
    else:
        form = PasswordValidationForm()
    return render(request,'django_forms.html',{'form':form})