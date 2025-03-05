from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path(
        "",
        views.home_page,
        name="index"
    ),
    path(
        "create-new-task/",
        views.create_new_tasks,
        name="create-new-task"
    ),
    path(
        "complete-task",
        views.complete_task,
        name="complete-task"
    )
]