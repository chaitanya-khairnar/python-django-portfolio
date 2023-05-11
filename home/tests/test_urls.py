from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, detail


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_details_url_resolves(self):
        url = reverse('detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, detail)
