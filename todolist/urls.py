from django.urls import path
from . import views
urlpatterns = [
    path("",views.todolist_home,name='home'),
    path("login",views.userlogin,name="login"),
    path("register",views.register,name="register"),
    path("tasks",views.tasks,name="tasks"),
    path("addtask",views.addtask,name="add"),
    path("deletetask/<int:id>",views.deletetask,name="delete"),
    path("updatetask/<int:id>",views.updatetask,name="update"),
    path("verify",views.verification,name="verify"),
    path("employee/<int:id>",views.employee,name="employee"),
]
