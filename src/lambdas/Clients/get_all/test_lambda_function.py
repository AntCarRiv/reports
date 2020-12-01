from unittest import TestCase
from .lambda_function import lambda_handler


class Test(TestCase):

    def test_lambda_handler(self):
        response = lambda_handler({}, None)
        print(response)
