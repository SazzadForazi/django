from django.shortcuts import render,redirect
from user.forms import UserRegistrationForm
from user.models import User
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class UserRegistrationView(CreateView):
  form_class = UserRegistrationForm
  model = User
  success_url = '/'
  template_name = 'registration.html'
  
  
class UserLoginView(LoginView):
  redirect_authenticated_user = True
  template_name='login.html'
  def get_success_url(self):
    return reverse_lazy('index')
  def form_invalid(self, form):
    messages.error(self.request,'Invalid username or password')
    return self.render_to_response(self.get_context_data(form=form))
  
  
def UserLogoutView(request):
  logout(request)
  messages.warning(request, 'You have been logged out')
  return redirect('login')