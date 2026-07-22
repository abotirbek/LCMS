from django.urls import path
from django.views.generic import TemplateView
from accounts import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.get_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('send/', TemplateView.as_view(template_name='accounts/send.html'), name='send'),
    path('reset/', views.send_email_code, name='reset'),
    path('change_password/', views.change_password, name='change_password'),
]