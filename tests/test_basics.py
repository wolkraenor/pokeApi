import unittest
from flask import current_app
from app import app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_status(self):
        response = self.client.get("/status")
        self.assertTrue(response.status_code == 200)
