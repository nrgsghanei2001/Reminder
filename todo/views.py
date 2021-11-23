from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import *

def index_page(request):
    return render(request, 'todo/index.html')

def admin_page(request):
    return render(request)

def categories_page(request):
    return render(request, 'todo/categories.html')

class TaskList(ListView):
    queryset = Task.objects.order_by("-deadline")
    template_name = 'todo/tasks.html'


class TaskDetail(DetailView):
    model = Task
    template_name = 'todo/tasks_explanation.html'


def add_task_page(request):
    return render(request, 'todo/add_task.html')