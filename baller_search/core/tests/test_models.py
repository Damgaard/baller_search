from test_plus.test import TestCase

from .factories import NerdBallerFactory, PostFactory


class TestNerdBaller(TestCase):

    def test_unicode_preferring_known_as(self):
        user = NerdBallerFactory.build()
        self.assertTrue((str(user) == user.known_as))

    def test_unicode_using_username_if_no_known_as(self):
        user = NerdBallerFactory.build(known_as="")
        self.assertTrue((str(user) == user.username))


class TestPost(TestCase):

    def test_unicode(self):
        post = PostFactory.build()
        self.assertTrue(str(post) == post.title)
