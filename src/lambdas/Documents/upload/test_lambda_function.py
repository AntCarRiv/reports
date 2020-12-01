from unittest import TestCase
from .lambda_function import lambda_handler
from tools_lambda.generic_tools import get_status_code


class Test(TestCase):
    def test_lambda_function(self):
        response = lambda_handler({}, None)
        self.assertEqual(200, get_status_code(response))
