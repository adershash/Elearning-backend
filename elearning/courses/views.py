from django.shortcuts import render
from rest_framework import mixins,generics
from .serializer import CourseSerializer
from .models import Courses

# Create your views here.

#mixins
class Course(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
#generics

class CourseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer
    lookup_field= 'pk'