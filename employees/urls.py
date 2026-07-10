from django.urls import path
from employees import views

urlpatterns = [
    path('department_list/', views.get_department, name='department_list'),
    path('create_department/', views.create_department, name='create_department'),
    path('read_department/<int:pk>/', views.read_department, name='read_department'),
    path('update_department/<int:pk>/', views.update_department, name='update_department'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),

    path('specialization_list/', views.get_specialization, name='specialization_list'),
    path('create_specialization/', views.create_specialization, name='create_specialization'),
    path('read_specialization/<int:pk>/', views.read_specialization, name='read_specialization'),
    path('update_specialization/<int:pk>/', views.update_specialization, name='update_specialization'),
    path('delete_specialization/<int:pk>/', views.delete_specialization, name='delete_specialization'),

    path('employee_list/', views.get_employee, name='employee_list'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('read_employee/<int:pk>/', views.read_employee, name='read_employee'),
    path('update_employee/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),
]
