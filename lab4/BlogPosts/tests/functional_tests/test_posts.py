import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

from BlogPosts.models import CustomUser


class TestPostsPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('data/files/chromedriver.exe')
        self.user = User.objects.create_superuser(
            username='user', email='user@email.com',
            password='User123!', id=1, )
        self.custom_user = CustomUser.objects.create(user_id=1,
                                                     photo='photos/blank-profile-picture-973460_640.png',
                                                     name='User',
                                                     surname='User', skills='Coding')
        self.client.login(username='user', password='User123!')
        cookie = self.client.cookies['sessionid']
        self.browser.get(
            self.live_server_url + '/posts/')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()
        self.browser.get(self.live_server_url + '/posts/')

    def test_posts(self):
        title = self.browser.find_element(by=By.TAG_NAME, value="h2")
        time.sleep(2)
        self.assertEquals(title.text, "Posts")

    def test_posts_navigation_to_profile(self):
        time.sleep(2)
        self.browser.find_element(by=By.CLASS_NAME, value="profile-page").click()
        time.sleep(2)
        self.assertEquals(self.browser.current_url, self.live_server_url + '/profile/')

    def test_posts_navigation_to_add_post(self):
        time.sleep(2)
        self.browser.find_element(by=By.CLASS_NAME, value="add-post-page").click()
        time.sleep(2)
        self.assertEquals(self.browser.current_url, self.live_server_url + '/add/post/')

    def test_posts_navigation_to_block_users_page(self):
        time.sleep(2)
        self.browser.find_element(by=By.CLASS_NAME, value="block-users-page").click()
        time.sleep(2)
        self.assertEquals(self.browser.current_url, self.live_server_url + '/blockedUsers/')

    def tearDown(self):
        self.browser.close()
        self.client.logout()
        User.objects.all().delete()
        CustomUser.objects.all().delete()
