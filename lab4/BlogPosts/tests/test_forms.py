from django.test import TestCase, Client
from django.contrib.auth.models import User
from BlogPosts.forms import CustomUserForm, PostForm
from django.core.files.uploadedfile import InMemoryUploadedFile
from BlogPosts.models import CustomUser


class TestForm(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='user', email='user@email.com',
            password='User123!')
        self.blocked_user = User.objects.create_user(
            username='blocked_user', email='blocked_user@email.com',
            password='BlockedUser123!')
        self.custom_user = CustomUser.objects.create(user_id=1,
                                                     photo='data/photos/blank-profile-picture-973460_640.png',
                                                     name='User',
                                                     surname='User')
        self.client.login(username='user', password='User123!')

    def test_users_exist(self):
        self.assertTrue(User.objects.filter(username=self.user.username).exists())
        self.assertTrue(User.objects.filter(username=self.blocked_user.username).exists())
        self.assertTrue(CustomUser.objects.filter(user_id=self.custom_user.id).exists())

    def test_post_form_valid_data(self):
        fp = open('data/files/index.jpg')
        fp1 = InMemoryUploadedFile(fp, None, 'index.jpg', 'image/jpg', fp.buffer.__sizeof__(), None)
        form = PostForm(data={
            'title': 'Post',
            'content': 'Content'
        }, files={'file': fp1})

        self.assertTrue(form.is_valid(),
                        msg=f"form should have been valid, but contains errors: {form.errors}")

    def test_post_form_no_data(self):
        form = PostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_custom_users_form_valid_data(self):
        form = CustomUserForm(data={
            'blocked_user': [self.blocked_user.id]
        })

        self.assertTrue(form.is_valid(),
                        msg=f"form should have been valid, but contains errors: {form.errors}")

    def test_custom_users_form_no_data(self):
        form = CustomUserForm(data={})

        self.assertTrue(form.is_valid())

    def tearDown(self):
        self.client.logout()
        User.objects.all().delete()
        CustomUser.objects.all().delete()
