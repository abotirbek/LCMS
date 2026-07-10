from django.urls import path
from centers import views

urlpatterns = [
    path('', views.get_center, name='center_list'),
    path('create_center/', views.create_center, name='create_center'),
    path('read_center/', views.read_center, name='read_center'),
    path('update_center/', views.update_center, name='update_center'),
    path('delete_center/', views.delete_center, name='delete_center'),

    path('branch_list/', views.get_branch, name='branch_list'),
    path('create_branch/', views.create_branch, name='create_branch'),
    path('read_branch/', views.read_branch, name='read_branch'),
    path('update_branch/', views.update_branch, name='update_branch'),
    path('delete_branch/', views.delete_branch, name='delete_branch'),

    path('room_list/', views.get_room, name='room_list'),
    path('create_room/', views.create_room, name='create_room'),
    path('read_room/', views.read_room, name='read_room'),
    path('update_room/', views.update_room, name='update_room'),
    path('delete_room/', views.delete_room, name='delete_room'),
]