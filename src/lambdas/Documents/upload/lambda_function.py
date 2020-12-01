from tools_lambda import decorators
from tools_lambda.generic_tools import get_logger

LOGGER = get_logger()


@decorators.web_response
def lambda_handler(event, context):
    return 200, 'ok'
