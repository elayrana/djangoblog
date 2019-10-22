from blog.models import Post
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secret',
        )

        self.post = Post.objects.create(
            title='This is a test',
            body='Nice body content',
            author=self.user,
        )
    
    def test_string_representation(self):
        post = Post(title='This is a test')
        self.assertEqual(str(post),post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'This is a test')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog/home.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/blog/post/1/')
        no_response = self.client.get('/blog/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'This is a test')
        self.assertTemplateUsed(response, 'blog/post.html')
    