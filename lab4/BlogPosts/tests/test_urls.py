from django.test import SimpleTestCase
from django.urls import reverse, resolve
from BlogPosts.views import posts, profile, add_post, blocked_users


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.posts_url = reverse('posts')
        self.profile_url = reverse('profile')
        self.add_post_url = reverse('add_post')
        self.blocked_users_url = reverse('blocked_users')

    def test_posts_url_resolves(self):
        print(resolve(self.posts_url))
        self.assertEquals(resolve(self.posts_url).func, posts)

    def test_profile_url_resolves(self):
        print(resolve(self.profile_url))
        self.assertEquals(resolve(self.profile_url).func, profile)

    def test_add_post_url_resolves(self):
        print(resolve(self.add_post_url))
        self.assertEquals(resolve(self.add_post_url).func, add_post)

    def test_blocked_users_url_resolves(self):
        print(resolve(self.blocked_users_url))
        self.assertEquals(resolve(self.blocked_users_url).func, blocked_users)
