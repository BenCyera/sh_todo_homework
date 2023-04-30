from django.urls import path
from articles import views

urlpatterns = [
    path('todolist/', views.TodoList.as_view(), name='article_view'),
    path('todofix/<int:Todo_id>/', views.TodoFix.as_view(), name='article_detail_view'),
]