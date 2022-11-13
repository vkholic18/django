from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from  . views import StudentViewSet_read

router=DefaultRouter()
router.register("students",views.StudentViewSet)

router.register("studentsread",views.StudentViewSet_read)



urlpatterns = [
    path("",include(router.urls)),





]
