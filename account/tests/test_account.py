from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from account.models import CustomUser, Organization
from account.serializers import CustomUserSerializer


class AccountApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(email='admin@yandex.ru')
        self.url = reverse('user_settings', kwargs={'pk': f'{self.user.id}'})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post(self):
        response = self.client.post(self.url, {
            "last_name": "Beliy",
        })


class OrgansationTestCase(APITestCase):
    def setUp(self) -> None:
        self.org = Organization.objects.create(name='some name')
        self.url = reverse('organisation_settings', kwargs={'pk': self.org.id})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post(self):
        response = self.client.post(self.url, {'name': 'some name', 'unp': '123adas'})
        print(response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

