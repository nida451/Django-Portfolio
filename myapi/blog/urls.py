from django.urls import path, include
from .views import PostListCreateView, PostDetailView, CreateUserView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', PostListCreateView, basename='blogpost')
router.register(r'posts/<int:pk>/', PostDetailView, basename='blogpost-detail')
router.register(r'register/', CreateUserView, basename='register')


urlpatterns = [
    path('', include(router.urls)),
]
