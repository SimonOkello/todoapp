from django.urls import path
from .views import (
    index,
    updateTodo,
    deleteTodo,
)
app_name = 'tasks'
urlpatterns = [
    path('', index, name='todo-list' ),
    path('<pk>/update/', updateTodo, name='update-todo' ),
    path('<pk>/delete/', deleteTodo, name='delete-todo' ),

]