from unittest import TestCase

from models.basemodel import database
from models.models import Clients
from models.tools_models import transaction_for_test
from tools_lambda.generic_tools import get_mty_datetime

from .lambda_function import lambda_handler


class Test(TestCase):

    @transaction_for_test(database=database)
    def test_lambda_handler(self):
        client_id = Clients.insert(names='Carlos', last_name='Rivera', create_at=get_mty_datetime()).execute()
        lambda_handler({"body": {"client_id": client_id}}, ())
