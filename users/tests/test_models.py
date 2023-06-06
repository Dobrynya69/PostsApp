from django.test import TestCase
from django.contrib.auth import get_user_model

class TestModels(TestCase):
    
    def setUp(self):
        get_user_model().objects.create_user(
            username='User',
            email='email@gmail.com',
            password='passwordUser'
        )


    def test_custom_user_model(self):
        self.assertEqual(get_user_model().objects.get(username='User').email, 'email@gmail.com')