from rest_framework import serializers
from .models import Users
from courses.serializer import CourseSerializer

class UserSerializer(serializers.ModelSerializer):
    reg_courses=CourseSerializer(many=True,read_only=True)
    class Meta:
        model=Users
        fields='__all__'