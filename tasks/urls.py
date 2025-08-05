from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<str:pk>/', views.task_update, name='task_update'),
    path('delete/<str:pk>/', views.task_delete, name='task_delete'),
    path('api/tasks/', api_views.api_task_list, name='api_task_list'),
    path('api/tasks/create/', api_views.api_task_create, name='api_task_create'),
    path('api/tasks/<int:pk>/', api_views.api_task_detail, name='api_task_detail'),
]
