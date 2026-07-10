from django.urls import path
from students import views

urlpatterns = [
    path('student_list/', views.get_student, name='student_list'),
    path('create_student/', views.create_student, name='create_student'),
    path('read_student/<int:pk>/', views.read_student, name='read_student'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),

    path('enrollment_list/', views.get_enrollment, name='enrollment_list'),
    path('create_enrollment/', views.create_enrollment, name='create_enrollment'),
    path('read_enrollment/<int:pk>/', views.read_enrollment, name='read_enrollment'),
    path('update_enrollment/<int:pk>/', views.update_enrollment, name='update_enrollment'),
    path('delete_enrollment/<int:pk>/', views.delete_enrollment, name='delete_enrollment'),

    path('attendance_list/', views.get_attendance, name='attendance_list'),
    path('create_attendance/', views.create_attendance, name='create_attendance'),
    path('read_attendance/<int:pk>/', views.read_attendance, name='read_attendance'),
    path('update_attendance/<int:pk>/', views.update_attendance, name='update_attendance'),
    path('delete_attendance/<int:pk>/', views.delete_attendance, name='delete_attendance'),
]
