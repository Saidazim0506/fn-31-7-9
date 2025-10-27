from rest_framework import serializers
from .models import Student, Course, Teacher

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    address = serializers.CharField

class CourseSerializer(serializers.Serializer):
    title = serializers.CharField()
    descriptions = serializers.CharField()
    price = serializers.IntegerField()

class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    subject = serializers.CharField()
    experience_years = serializers.IntegerField()
