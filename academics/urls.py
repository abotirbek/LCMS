from django.urls import path
from academics import views

urlpatterns = [
    path('course_list/', views.get_course, name='course_list'),
    path('create_course/', views.create_course, name='create_course'),
    path('read_course/<int:pk>/', views.read_course, name='read_course'),
    path('update_course/<int:pk>/', views.update_course, name='update_course'),
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'),

    path('group_list/', views.get_group, name='group_list'),
    path('create_group/', views.create_group, name='create_group'),
    path('read_group/<int:pk>/', views.read_group, name='read_group'),
    path('update_group/<int:pk>/', views.update_group, name='update_group'),
    path('delete_group/<int:pk>/', views.delete_group, name='delete_group'),
]