from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('teacher_list/', views.get_teacher, name='teacher_list'),
    path('create_teacher/', views.create_teacher, name='create_teacher'),
    path('read_teacher/<int:pk>/', views.read_teacher, name='read_teacher'),
    path('update_teacher/<int:pk>/', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:pk>/', views.delete_teacher, name='delete_teacher'),

    path('employee_list/', views.get_employee, name='employee_list'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('read_employee/<int:pk>/', views.read_employee, name='read_employee'),
    path('update_employee/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),

    path('student_list/', views.get_student, name='student_list'),
    path('create_student/', views.create_student, name='create_student'),
    path('read_student/<int:pk>/', views.read_student, name='read_student'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),

    path('department_list/', views.get_department, name='department_list'),
    path('create_department/', views.create_department, name='create_employee'),
    path('read_department/<int:pk>/', views.read_department, name='read_department'),
    path('update_department/<int:pk>/', views.update_department, name='update_department'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),

    path('specialization_list/', views.get_specialization, name='specialization_list'),
    path('create_specialization/', views.create_specialization, name='create_specialization'),
    path('read_specialization/<int:pk>/', views.read_specialization, name='read_specialization'),
    path('update_specialization/<int:pk>/', views.update_specialization, name='update_specialization'),
    path('delete_specialization/<int:pk>/', views.delete_specialization, name='delete_specialization'),
]