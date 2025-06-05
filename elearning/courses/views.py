from django.shortcuts import render,get_object_or_404
from rest_framework import mixins,generics
from .serializer import CourseSerializer
from .models import Courses
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# #mixins
# class Course(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Courses.objects.all()
#     serializer_class=CourseSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    
# #generics

# class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Courses.objects.all()
#     serializer_class=CourseSerializer
#     lookup_field= 'pk'


#ViewSets example
"""
class Course(viewsets.ViewSet):
    def list(self,request):
        queryset=Courses.objects.all()
        serializer=CourseSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def retrieve(self,request,pk=None):
        course=get_object_or_404(Courses,pk=pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
"""
#ModelViewSets example

class Course(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer