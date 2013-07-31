"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            'test',
            'test@test.com',
            'secret')


    """Check that all the Non Logged users has not access to the backend
    and check that the logged users could access."""
    def test_login_for__backend_main_no_logged(self):
        url_to_go = reverse('backend_main')
        test_output = [
                ('http://testserver/accounts/login/?next=/linkedin/backend/',
                302)
                ]

        response = self.client.get(url_to_go, follow=True)
        self.assertEqual(response.redirect_chain, test_output)



    def test_login_for__backend_main_logged(self):
        url_to_go = reverse('backend_main')
        test_output = []

        self.client.login(username='test', password='secret')
        response = self.client.get(url_to_go, follow=True)
        self.assertEqual(response.redirect_chain, test_output)
        self.assertTrue('logout' in response.content)



    def test_login_for__backend_linkedin_no_logged(self):
        url_to_go = reverse('backend_linkedin')
        test_output = [
                ('http://testserver/accounts/login/?next=/linkedin/backend/linkedin',
                302)
                ]

        response = self.client.get(url_to_go, follow=True)
        self.assertEqual(response.redirect_chain, test_output)



    def test_login_for__backend_linkedin_logged(self):
        url_to_go = reverse('backend_linkedin')
        url_to_backend_main = reverse('backend_main')
        test_output = []

        self.client.login(username='test', password='secret')
        response = self.client.get(url_to_go, follow=True)
        self.assertEqual(response.redirect_chain, test_output)
        self.assertTrue(url_to_backend_main in response.content)



    def test_login_for__backend_socialbuttons_no_logged(self):
        url_to_go = reverse('backend_social_buttons')
        test_output = [
                ('http://testserver/accounts/login/?next=/linkedin/backend/social_section',
                302)
                ]

        response = self.client.get(url_to_go, follow=True)
        self.assertEqual(response.redirect_chain, test_output)



    def test_login_for__backend_socialbuttons_logged(self):
        url_to_go = reverse('backend_social_buttons')
        url_to_backend_main = reverse('backend_main')
        test_output = []

        self.client.login(username='test', password='secret')
        response = self.client.get(url_to_go, follow=True)
        self.assertEqual(response.redirect_chain, test_output)
        self.assertTrue(url_to_backend_main in response.content)



    def test_login_for__backend_sections_no_logged(self):
        url_to_go = reverse('backend_sections')
        test_output = [
                ('http://testserver/accounts/login/?next=/linkedin/backend/sections_setup',
                302)
                ]

        response = self.client.get(url_to_go, follow=True)
        self.assertEqual(response.redirect_chain, test_output)



    def test_login_for__backend_sections_logged(self):
        url_to_go = reverse('backend_sections')
        url_to_backend_main = reverse('backend_main')
        test_output = []

        self.client.login(username='test', password='secret')
        response = self.client.get(url_to_go, follow=True)
        self.assertEqual(response.redirect_chain, test_output)
        self.assertTrue(url_to_backend_main in response.content)



