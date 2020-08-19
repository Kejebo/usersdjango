from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task

class CreateTask(CreateView):
    model= Task
    template_name='task/create_task.html'
    fields= '__all__'
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)    
    
class ListTask(ListView):
    model=Task
    template_name='task/'
    def get_queryset(self):
        return self.model.objects.filter(user=user).order_by('-date')
    