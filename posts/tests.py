from django.test import TestCase
from .models import Post
from http import HTTPStatus

# Create your tests here.

class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)
    
    def test_str_rep_of_objects(self):
        post = Post.objects.create(
            title='Test Title',
            body='Test Body'
        )

        self.assertEqual(str(post), post.title)

class HomePageTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(
            title='Sample Post 1',
            body='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
        )

        Post.objects.create(
            title='Sample Post 2',
            body='Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
        )

    def test_hompe_page_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)