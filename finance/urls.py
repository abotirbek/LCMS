from django.urls import path
from finance import views

urlpatterns = [
    path('invoice_list/', views.get_invoice, name='invoice_list'),
    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('read_invoice/<int:pk>/', views.read_invoice, name='read_invoice'),
    path('update_invoice/<int:pk>/', views.update_invoice, name='update_invoice'),
    path('delete_invoice/<int:pk>/', views.delete_invoice, name='delete_invoice'),

    path('payment_invoice_list/', views.get_payment_invoice, name='payment_invoice_list'),
    path('create_payment_invoice/', views.create_payment_invoice, name='create_payment_invoice'),
    path('read_payment_invoice/<int:pk>/', views.read_payment_invoice, name='read_payment_invoice'),
    path('update_payment_invoice/<int:pk>/', views.update_payment_invoice, name='update_payment_invoice'),
    path('delete_payment_invoice/<int:pk>/', views.delete_payment_invoice, name='delete_payment_invoice'),

    path('payment_list/', views.get_payment, name='payment_list'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('read_payment/<int:pk>/', views.read_payment, name='read_payment'),
    path('update_payment/<int:pk>/', views.update_payment, name='update_payment'),
    path('delete_payment/<int:pk>/', views.delete_payment, name='delete_payment'),
]
