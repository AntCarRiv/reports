from unittest import TestCase

from tools_lambda.generic_tools import get_status_code

from .lambda_function import lambda_handler
from models.tools_models import transaction_for_test
from models.basemodel import database


class Test(TestCase):
    @transaction_for_test(database=database)
    def test_lambda_handler(self):
        response = lambda_handler({"body": {"names": "Carlos",
                                            "last_name": "Añorve"}}, None)
        self.assertEqual(200, get_status_code(response))
