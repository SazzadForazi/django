from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="Enter your Name:")
    email = forms.EmailField(label = "User Email")
    