import unittest
import json
from flask import current_app
from app import app
from tests.test_basics import BasicsTestCase
from tests.test_service import ServiceTestCase

BasicsTestCase()
#ServiceTestCase()

if __name__ == "__main__":
    unittest.main()
