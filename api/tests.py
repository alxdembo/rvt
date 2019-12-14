import base64
import json
import urllib.parse
from django.contrib.auth.models import User
from django.test import TestCase

from django.urls import reverse

from helpers.test_helpers import load_testing_json


class RestApiNesterTest(TestCase):
    header = None
    nesting_level_url = None

    def setUp(self) -> None:
        username = 'user'
        password = 'pass'

        self.user = User.objects.create_user(username=username, password=password)
        encoded_bytes = base64.b64encode(f'{username}:{password}'.encode("utf-8"))
        encoded_credentials = str(encoded_bytes, "utf-8")
        self.header = {'HTTP_AUTHORIZATION': f'Basic ' + encoded_credentials}
        self.nesting_level_url = self.__get_nesting_levels_url()

    @staticmethod
    def __get_nesting_levels_url():
        params = (('q[]', 'currency'), ('q[]', 'country'), ('q[]', 'city'))  # forms an array as a parameter
        nesting_levels = urllib.parse.urlencode(params)
        return reverse('api_nest') + '?' + nesting_levels

    def test_nesting(self):
        request_body = load_testing_json('input/original_task.json')
        response = self.client.post(
            self.nesting_level_url,
            data=request_body,
            content_type='application/json',
            **self.header)

        actual = json.loads(response.content)
        expected = load_testing_json('output/original_task.json')
        self.assertEqual(expected, actual)
        self.assertEqual(200, response.status_code)

    def test_nesting_key_error(self):
        url = reverse('api_nest') + '?q[]=123'
        request_body = load_testing_json('input/original_task.json')
        response = self.client.post(url, data=request_body, content_type='application/json', **self.header)

        self.assertEqual(422, response.status_code)

    def test_nesting_empty_body(self):
        request_body = {}
        response = self.client.post(
            self.nesting_level_url,
            data=request_body,
            content_type='application/json',
            **self.header)

        self.assertEqual(422, response.status_code)

    def test_nesting_empty_nesting_levels(self):
        request_body = load_testing_json('input/original_task.json')
        url = reverse('api_nest')
        response = self.client.post(url, data=request_body, content_type='application/json', **self.header)

        self.assertEqual(422, response.status_code)

    def test_nesting_malformed_nesting_levels(self):
        request_body = load_testing_json('input/original_task.json')
        url = reverse('api_nest') + '?qqq=123'
        response = self.client.post(url, data=request_body, content_type='application/json', **self.header)

        self.assertEqual(422, response.status_code)

    def test_auth(self):
        header = {'HTTP_AUTHORIZATION': f'Basic 1234'}
        response = self.client.post(reverse('api_nest'), **header)

        self.assertEqual(401, response.status_code)

    def tearDown(self) -> None:
        self.user = None
        self.header = None
        self.nesting_level_url = None
