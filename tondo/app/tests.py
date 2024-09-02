from django.test import TestCase
from django.test.client import RequestFactory
from .models import Data
from .views import get_details, save_details


# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Data.objects.create(userid=1, roles="test")

    def test_add_role(self):
        ob = Data.objects.get(userid=1)
        self.assertIsNone(ob.add_role("test2"))


class ViewTest(TestCase):

    def setUp(self):
        Data.objects.create(userid=1, roles="test")
        self.factory = RequestFactory()

    def test_get_details(self):
        request = self.factory.get('app/data/')
        expected_data = {'id': 1, 'userid': 1, 'roles': 'test'}

        # Test get_details() as userid 1 is in DB
        response = get_details(request=request, userid=1)
        with self.subTest("response code: "):
            self.assertEqual(response.status_code, 200)
        with self.subTest("response data: "):
            self.assertEqual(response.data, expected_data)

    def test_get_details_error(self):
        request = self.factory.get('app/data/')

        # Test get_details() as userid 2 not found in DB
        response = get_details(request=request, userid=2)
        with self.subTest("response code: "):
            self.assertEqual(response.status_code, 404)
        with self.subTest("response data: "):
            self.assertIsNone(response.data)

    def test_save_details(self):
        data = {'roles': 'test2'}
        request = self.factory.post('app/data/save/', data=data, content_type='application/json')

        expected_data = {'id': 1, 'userid': 1, 'roles': 'test, test2'}

        response = save_details(request=request, userid=1)
        with self.subTest("response code: "):
            self.assertEqual(response.status_code, 201)
        with self.subTest("response data: "):
            self.assertEqual(response.data, expected_data)

    def test_save_details_new_userid(self):
        data = {'userid': 2, 'roles': 'test3'}
        request = self.factory.post('app/data/save/', data=data, content_type='application/json')

        expected_data = {'id': 2, 'userid': 2, 'roles': 'test3'}

        response = save_details(request=request, userid=2)
        with self.subTest("response code: "):
            self.assertEqual(response.status_code, 201)
        with self.subTest("response data: "):
            self.assertEqual(response.data, expected_data)
