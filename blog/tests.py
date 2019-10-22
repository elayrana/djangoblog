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
        self.assertEqual(str(post), post.title)

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

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/blog/post/1/')

    def test_post_create_view(self):  # new
        response = self.client.post(reverse('blog:new_post'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):  # new
        response = self.client.post(reverse('blog:update_post', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 200)

    def test_post_delete_view(self):  # new
        response = self.client.get(reverse('blog:delete_post', args='1'))
        self.assertEqual(response.status_code, 200)
