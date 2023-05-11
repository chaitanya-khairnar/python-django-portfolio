from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_project_list_GET(self):
        client = Client()

        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
