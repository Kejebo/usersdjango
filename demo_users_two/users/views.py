from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegisterForm,LoginForm, UpdatePasswordForms
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    View,
    CreateView,
    TemplateView
)
from .models import CustomUser

class Home(LoginRequiredMixin, TemplateView):
    template_name='home.html'
    login_url= reverse_lazy('app_users:login')
    
class RegisterUser(FormView):
    template_name='user/register.html'
    form_class= UserRegisterForm
    success_url='home.html'
    
    def form_valid(self, form):
        password1=form.cleaned_data['password1']
        password2=form.cleaned_data['password2']
       
        if password1 == password2:
            user=CustomUser.objects.create_user(
                form.cleaned_data['email'],
                form.cleaned_data['username'],
                form.cleaned_data['password1'],
                
            )
            
        return super(RegisterUser,self).form_valid(form)
    
class Login(FormView):
    template_name='login.html'
    form_class= LoginForm
    success_url=reverse_lazy('app_users:home')
    
    def form_valid(self, form):
        user=authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request,user)
        return super(Login,self).form_valid(form)

class UpdatePassword(LoginRequiredMixin,FormView):
    template_name='user/update_password.html'
    form_class= UpdatePasswordForms
    success_url=reverse_lazy('app_users:login')
    login_url=reverse_lazy('app_users:login')
    def form_valid(self, form):
        data_user=self.request.user
        user=authenticate(
            email=data_user.email,
            password=form.cleaned_data['password1']
        )
        
        if user:
            new_password=form.cleaned_data['password2']
            data_user.set_password(new_password)
            data_user.save()
            logout(self.request)
        else:
            self.template_name=reverse_lazy('app_users:changes_password') 
        return super(UpdatePassword,self).form_valid(form)


class Logout(View):
    def get(self, request,*arg,**kwarg):
        logout(request)
        return HttpResponseRedirect(
            reverse('app_users:login')
        )