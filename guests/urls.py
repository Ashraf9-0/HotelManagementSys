from django.urls import path
from . import views

urlpatterns = [
    path('', views.guest_list, name='guest_list'),
    path('register/', views.register_guest, name='register_guest'),
    path('view/<int:pk>/', views.guest_detail, name='guest_detail'),
    path('edit/<int:pk>/', views.edit_guest, name='edit_guest'),
    path('delete/<int:pk>/', views.delete_guest, name='delete_guest'),
]