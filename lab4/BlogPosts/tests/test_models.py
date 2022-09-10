from django.test import TestCase
from django.contrib.auth.models import User
from BlogPosts.models import CustomUser, Post, Comment


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user",
                                             email="user@email.com", password="User123!")
        self.custom_user = CustomUser.objects.create(
            user_id=1, photo="files/images.jpg", name="User", surname="User")
        self.post = Post.objects.create(title="Post", user_id=1, content="Content",
                                        file="data/files/index.jpg")
        self.comment = Comment.objects.create(author_id=1, content="Content", post_id=1)

    def test_user_exists(self):
        self.assertTrue(User.objects.filter(username=self.user.username).exists())

    def test_custom_user_exists(self):
        self.assertTrue(User.objects.filter(id=self.custom_user.id).exists())

    def test_post_exists(self):
        self.assertTrue(Post.objects.filter(id=self.post.id).exists())

    def test_comment_exists(self):
        self.assertTrue(Comment.objects.filter(id=self.comment.id).exists())

    def test_custom_user_has_post(self):
        self.assertEquals(self.custom_user.post_set.count(), 1)

    def test_custom_user_has_comment(self):
        self.assertEquals(self.custom_user.comment_set.count(), 1)

    def tearDown(self):
        User.objects.all().delete()
        CustomUser.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()
