from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . serializer import  StudentSerializer
from rest_framework.response import Response
from rest_framework import status,generics,viewsets
from rest_framework.decorators import api_view
# Create your views here.
def rest_home(request):
    return HttpResponse("Rest Home")


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer

class StudentViewSet_read(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer



'''
class student_list(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer


class student_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class =StudentSerializer

@api_view(["GET","POST"])
def student_list(request):

    if request.method=="GET":
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serilaizer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(["GET","PUT","DELETE"])
def student_details(request,id):
    try:
        student=Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    elif request.method=="PUT":
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
