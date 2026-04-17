from django.urls import path
from . import views


urlpatterns = [
    path('', views.room_list, name='rooms_list'),
    path('rooms/', views.register_room, name='add_room'),
    path('view/<int:pk>/', views.room_detail, name='view_room'),
    path('rooms/edit/<int:pk>/', views.edit_room, name='edit_room'),
    path('rooms/delete/<int:pk>/', views.delete_room, name='delete_room'),
]
