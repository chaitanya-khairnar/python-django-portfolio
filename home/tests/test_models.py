from django.test import TestCase
from home.models import Experience


class TestModels(TestCase):

    def setUp(self):
        self.experience = Experience.objects.create(
            job_experience='experience-1',
            # company = 'ABC'
        )

    def test_experience_is_assigned(self):
        job_experience = {'Experience': 'experience-1'}
