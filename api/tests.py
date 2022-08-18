from rest_framework import status

from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'testcase', 'password': '3kvnor4nvornonre', 'role': 'Employee', }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
