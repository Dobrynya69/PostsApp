from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import *

class TestUrls(SimpleTestCase):

    def test_home_page_resolved(self):
        url = reverse('home_page')
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_user_profile_page_resolved(self):
        url = reverse('user_profile', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, UserProfilePageView)