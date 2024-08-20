from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),  # URL for listing all posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # URL for viewing a single post
    path('post/new/', views.post_new, name='post_new'),  # URL for adding a new post
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),  # URL for adding a comment to a post
]
