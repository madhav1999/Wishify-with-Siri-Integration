from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#for accessing login_required decorator function
from django.contrib.auth.decorators import login_required

#for login creation separately for people instead of giving admin access
from django.contrib.auth.views import LoginView,LogoutView

#for signup creation separately for people instead of showing admin interface
from django.views.generic.edit import CreateView

#user creation function is a django function
from django.contrib.auth.forms import UserCreationForm



#libraries for class based views
from django.views.generic import TemplateView
   #mixin inplace of decorator function it is mixin class
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

# Create your views here.
####################################################
# def home(request):
#     return render(request, 'home/welcome.html',{'today': datetime.today()})
####################################################
#using decorators to allow this endpoint only if the user is logged in
####################################################
# @login_required(login_url='/admin') #-->if not login instead we get 404 error by specifying this we are redirected to this endpoint
# def authorized(request):
#     return render(request, 'home/authorized.html', {}) 
####################################################

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html' #for first function
    login_url = '/admin' #for second function, mixin class concept instead of decorators

####################################################

#login class
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

#logout class
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

#signup class
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/login'


