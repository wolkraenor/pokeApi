import json
from unittest import TestCase
from unittest.mock import patch
from app.adapter import PokemonsRequest
from tests.fixtures.mocks import API_MOCK_RESPONSE
from app import app


class ServiceTestCase(TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    @patch.object(PokemonsRequest, "request_data", return_value=API_MOCK_RESPONSE)
    def test_all_pokemons(self, mocked_request_data):
        mocked_request_data.return_value = API_MOCK_RESPONSE
        response = self.client.get('/pokemon')
        data = response.json
        print(data)
        self.assertTrue(mocked_request_data.called)
        self.assertTrue(response.status_code == 200)
        #self.assertEqual(data,)