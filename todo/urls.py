from django.urls import path
from .views import *
from . import admin

urlpatterns = [
    path('', index_page, name='index'),
    path('admin/', admin_page, name='admin'),
    path('categories/', CategoriesList.as_view(), name='categories'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('<int:pk>/', TaskDetail.as_view(), name="tasks_explanation"),
    path('add/task/', add_task_page, name='add_task'),
    # path('<int:pk>/', CategoriesDetail.as_view(), name='categories_detail'),
]
