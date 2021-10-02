from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:todo-list')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/todo-list.html', context)


def updateTodo(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=obj)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('tasks:todo-list')
    context = {'obj': obj, 'form': form}
    return render(request, 'tasks/update.html', context)


def deleteTodo(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('tasks:todo-list')
    context = {'obj': obj}
    return render(request, 'tasks/delete.html', context)
