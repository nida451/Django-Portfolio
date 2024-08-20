# blog/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Post

class BlogPostAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.blog_post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user
        )

    def test_create_blog_post(self):
        data = {"title": "New Post", "content": "This is a new post.", "author": "User1"}
        response = self.client.post('/api/posts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_blog_posts(self):
        response = self.client.get('/api/posts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_update_blog_post(self):
        url = f'/api/posts/{self.blog_post.id}/'
        data = {"title": "Updated Post","content": "This is updated post.", "author": "User1"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.blog_post.refresh_from_db()
        self.assertEqual(self.blog_post.title, "Updated Post")

    def test_delete_blog_post(self):
        url = f'/api/posts/{self.blog_post.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
