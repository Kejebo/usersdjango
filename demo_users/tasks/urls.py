from django.urls import path
from .views import HomePageView,CreateTask,UpdateTask

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('task/',CreateTask.as_view(), name='create_task'),
    path('task/<int:pk>',UpdateTask.as_view(), name='update_task')
]