from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile_view, profile_edit, home, chat_room, create_chat_room, add_profile_data, logout_view,chat_room_list, chat_room_detail

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('accounts/add_profile_data/', add_profile_data, name='profile_data'),
    path('accounts/profile/', profile_view, name='profile_view'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('create_chat_room/', create_chat_room, name='create_chat_room'),
    path('chat_room/<int:chat_room_id>/', chat_room, name='chat_room'),
    path('chat-rooms/<int:chat_room_id>', chat_room_detail, name='chat_room_detail'),
    path('chat-rooms/', chat_room_list, name='chat_room_list'),
]