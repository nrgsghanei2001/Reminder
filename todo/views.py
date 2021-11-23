from django.shortcuts import render

def index_page(request):
    return render(request, 'todo/index.html')

def admin_page(request):
    return render(request)

def categories_page(request):
    return render(request, 'todo/categories.html')

def tasks_page(request):
    return render(request, 'todo/tasks.html')