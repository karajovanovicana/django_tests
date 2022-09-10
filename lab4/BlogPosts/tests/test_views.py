from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from BlogPosts.models import CustomUser, Post


class TestViews(TestCase):

    def setUp(self):
        self.posts_url = reverse('posts')
        self.profile_url = reverse('profile')
        self.add_post_url = reverse('add_post')
        self.blocked_users_url = reverse('blocked_users')
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='user', email='user@email.com',
            password='User123!')
        self.blocked_user = User.objects.create_user(
            username='blocked_user', email='blocked_user@email.com',
            password='BlockedUser123!')
        self.custom_user = CustomUser.objects.create(user_id=1, photo='data/photos/blank-profile-picture-973460_640.png'
                                                     , name='User',
                                                     surname='User')
        self.client.login(username='user', password='User123!')

    def test_users_exist(self):
        self.assertTrue(User.objects.filter(username=self.user.username).exists())
        self.assertTrue(User.objects.filter(username=self.blocked_user.username).exists())
        self.assertTrue(CustomUser.objects.filter(user_id=self.custom_user.id).exists())

    def test_project_posts_GET(self):
        response = self.client.get(self.posts_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')

    def test_project_profile_GET(self):
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_project_add_post_POST(self):
        fp = 'data/files/text.txt'
        data = {
            'title': 'Post',
            'content': 'Post Content',
            'file': open(fp)
        }

        response = self.client.post(self.add_post_url, data, format='json')

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.profile_url)
        self.assertTrue(Post.objects.filter(user_id=self.custom_user.user_id).exists())

    def test_project_blocked_users_POST(self):
        data = {
            'blocked_user': self.blocked_user.id
        }
        response = self.client.post(self.blocked_users_url, data, format='json')

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, self.blocked_users_url)
        self.assertTrue(CustomUser.objects.filter(blocked_user=self.blocked_user).exists())

    def tearDown(self):
        self.client.logout()
        User.objects.all().delete()
        CustomUser.objects.all().delete()
