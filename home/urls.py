from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("about/",views.about,name='home'),
    path("projects",views.projects,name='home'),
    path("contact",views.contact,name='home'),
]
