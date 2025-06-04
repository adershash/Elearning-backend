from django.shortcuts import render
from .serializer import UserSerializer
from .models import Users
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.
@api_view(['GET','POST'])
def getUsers(request):
    if request.method=='GET':
        user=Users.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    

class UserDetails(APIView):
    def get_user(self,pk):
        try:
            user=Users.objects.get(pk=pk)
            return user
        except Users.DoesNotExist:
            return Http404

    def get(self,request,pk):
        user=self.get_user(pk)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        user=self.get_user(pk)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        user=self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)