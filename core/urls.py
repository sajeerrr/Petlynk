from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='user_login'),
    path('register/', views.register, name='register'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<str:username>/', views.reset_password, name='reset_password'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('send-bond-request/', views.send_bond_request, name='send_bond_request'),
    path('accept-bond/<int:bond_id>/', views.accept_bond, name='accept_bond'),
    path('chats/', views.chat_list, name='chat_list'),
    path('chat/<int:profile_id>/', views.chat_room, name='chat_room'),
    path('send-message/<int:profile_id>/', views.send_message, name='send_message'),
    path('get-new-messages/<int:profile_id>/', views.get_new_messages, name='get_new_messages'),
]
