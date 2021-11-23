from django.urls import path
from .views import *
from . import admin

urlpatterns = [
    path('', index_page, name='index'),
    path('admin/', admin_page, name='admin'),
    path('categories/', categories_page, name='categories'),
    path('tasks/', tasks_page, name='tasks'),
]
