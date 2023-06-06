from django.test import TestCase, Client
from django.urls import reverse
from users.views import *
from users.models import *
from django.contrib.auth import get_user_model


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.post(reverse('account_signup'), {
            'email': 'email@gmail.com',
            'username': 'TestUser',
            'first_name': 'First name',
            'last_name': 'Last name',
            'password1': 'passwordTest',
            'password2': 'passwordTest'
        })
        self.client.login(username='TestUser', password='password')

        self.home_page_url = reverse('home_page')
        self.user_profile_url = reverse('user_profile', kwargs={'pk': get_user_model().objects.get(username='TestUser').pk})


    def test_home_page_GET(self):
        response = self.client.get(self.home_page_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/home_page.html')


    def test_user_profile_GET_loged_in(self):
        response = self.client.get(self.user_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_profile.html')

    
    def test_user_profile_GET_do_not_loged_in(self):
        self.client.logout()
        response = self.client.get(self.user_profile_url)
        self.assertEqual(response.status_code, 302)
        self.client.login(username='TestUser', password='password')

    
    def test_user_profile_GET_wrong_pk(self):
        response = self.client.get(reverse('user_profile', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, 403)


    def test_user_profile_POST_loged_in(self):
        response = self.client.post(self.user_profile_url, {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.get(username='TestUser').first_name, 'NewFirstName')
        response = self.client.post(self.user_profile_url, {
            'first_name': 'First name',
            'last_name': 'Last name'
        })

    
    def test_user_profile_POST_do_not_loged_in(self):
        self.client.logout()
        response = self.client.post(self.user_profile_url, {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName'
        })
        self.assertEqual(response.status_code, 302)
        self.client.login(username='TestUser', password='password')

    
    def test_user_profile_POST_wrong_pk(self):
        response = self.client.post(reverse('user_profile', kwargs={'pk': 100}), {
            'first_name': 'NewFirstName',
            'last_name': 'NewLastName'
        })
        self.assertEqual(response.status_code, 403)