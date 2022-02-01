from django.test import TestCase
from rest_framework.test import APIRequestFactory




class AccountTest(TestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()

    def test_account_page(self):
        self.factory.get('/profile/')

    def tearDown(self) -> None:
        pass

