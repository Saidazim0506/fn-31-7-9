from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Course, Teacher
from .serializers import StudentSerializer, CourseSerializer, TeacherSerializer


class Student_list(APIView):
    def student_list(request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class Student_detail(APIView):
    def student_detail(request, pk):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)


class Course_list(APIView):
    def course_list(request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class Course_detail(APIView):
    def course_detail(request, pk):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class Teacher_list(APIView):
    def teacher_list(request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class Teacher_detail(APIView):
    def teacher_detail(request, pk):
        teacher = Teacher.objects.get(id=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
