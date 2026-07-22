from django.urls import path
from centers import views

urlpatterns = [
    path('', views.get_statistics, name='statistics'),

    path('', views.get_center, name='center_list'),
    path('create_center/', views.create_center, name='create_center'),
    path('read_center/<int:pk>/', views.read_center, name='read_center'),
    path('update_center/<int:pk>/', views.update_center, name='update_center'),
    path('delete_center/<int:pk>/', views.delete_center, name='delete_center'),

    path('branch_list/', views.get_branch, name='branch_list'),
    path('create_branch/', views.create_branch, name='create_branch'),
    path('read_branch/<int:pk>/', views.read_branch, name='read_branch'),
    path('update_branch/<int:pk>/', views.update_branch, name='update_branch'),
    path('delete_branch/<int:pk>/', views.delete_branch, name='delete_branch'),
]