from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView,UpdateView,DeleteView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomePageView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'home.html'
    context_object_name ='tasks'
    login_url = '/accounts/login/'
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.order_by('-date')
        else:
            return self.model.objects.filter(employee=self.request.user)

class CreateTask(CreateView):
   
    model= Task
    fields=['name','description','date','employee']
    template_name='task/create_task.html'
    success_url=reverse_lazy('home')

class UpdateTask(UpdateView):
   
    model= Task
    fields=['name','description','date','employee']
    template_name='task/create_task.html'
    success_url=reverse_lazy('home')
    
