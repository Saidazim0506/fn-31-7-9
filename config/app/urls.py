from django.urls import path
from .views import Student_list, Student_detail, Course_list, Course_detail, Teacher_list, Teacher_detail

urlpatterns = [
    path('students/', Student_list.as_view()),
    path('students/<int:pk>/', Student_detail.as_view()),

    path('courses/', Course_list.as_view()),
    path('courses/<int:pk>/', Course_detail.as_view()),

    path('teachers/', Teacher_list.as_view()),
    path('teachers/<int:pk>/', Teacher_detail.as_view()),
]
