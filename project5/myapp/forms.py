from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="Enter your Name:")
    email = forms.EmailField(label = "User Email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    age = forms.CharField()
    check = forms.BooleanField()
    birthday = forms.CharField()
    appointment = forms.CharField()
    