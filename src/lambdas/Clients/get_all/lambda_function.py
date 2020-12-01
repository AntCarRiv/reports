from models.models import Clients
from tools_lambda.generic_tools import get_logger
from tools_lambda.decorators import web_response

LOGGER = get_logger()


@web_response
def lambda_handler(event, context):
    result = Clients.select().dicts().get_all()
    return 200, result
