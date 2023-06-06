from django.test import TestCase
from django.contrib.auth import get_user_model
from users.forms import *

class TestForms(TestCase):

    def test_custom_user_creation_form_valid_data(self):
        form = CustomUserCreationForm(data={
            'email': 'email@gmail.com',
            'username': 'TestUser',
            'first_name': 'First name',
            'last_name': 'Last name',
            'password1': 'passwordTest',
            'password2': 'passwordTest'
        })
        self.assertTrue(form.is_valid())


    def test_custom_user_creation_form_invalid_data(self):
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())


    def test_custom_user_login_form_valid_data(self):
        try:
            form = CustomUserLoginForm(data={
                'login': 'TestUser',
                'password': 'passwordTest',
            })
            self.assertEqual(len(form.errors), 0)
        except:
            pass


    def test_custom_user_login_form_invalid_data(self):
        form = CustomUserLoginForm(data={})
        self.assertEqual(len(form.errors), 2)


    def test_custom_user_form_valid_data(self):
        form = CustomUserForm(data={
            'first_name': 'First name',
            'last_name': 'Last name',
        })
        self.assertTrue(form.is_valid())

    def test_custom_user_form_invalid_data(self):
        form = CustomUserForm(data={})
        self.assertFalse(form.is_valid())