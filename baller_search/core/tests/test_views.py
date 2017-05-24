from test_plus.test import TestCase

from django.core.urlresolvers import reverse


class TestViewsSimple(TestCase):

    def test_home(self):
        result = self.client.get(reverse('home'))
        self.assertTrue(result.status_code == 200)

    def test_about(self):
        result = self.client.get(reverse('about'))
        self.assertTrue(result.status_code == 200)

    def test_no_admin_endpoint_in_prod(self):
        result = self.client.get('/admin/')
        self.assertTrue(result.status_code == 404)
