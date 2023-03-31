from django.test import TestCase

from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@example.com',
            password='password123'
        )

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, get_user_model()))
        self.assertEqual(self.user.__str__(), self.user.username)
