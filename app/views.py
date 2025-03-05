from django.shortcuts import render, redirect
from .models import Task, ToDoList
from django.urls import reverse


def home_page(request):
    user = request.user
    todo_list = ToDoList.objects.get(user=user)
    tasks = Task.objects.filter(todo_list=todo_list)
    context = {"task_list": tasks}
    return render(request, 'home.html', context)


def create_new_tasks(request):
    user = request.user
    todo_list = ToDoList.objects.get(user=user)
    task = request.POST.get("task_title")
    Task.objects.create(
        todo_list = todo_list,
        title = task,
    )
    return redirect(reverse("app:index"))

def complete_task(request):
    ...



