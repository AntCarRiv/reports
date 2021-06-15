from models.models import Clients
from tools_lambda.decorators import web_response
from tools_lambda.generic_tools import (get_body, get_logger)

from .model_event import BodyNewClient

LOGGER = get_logger(__name__)


@web_response
def lambda_handler(event, context):
    try:
        body = BodyNewClient(**get_body(event))
    except TypeError as e:
        LOGGER.error(str(e))
        return 400, f'Bad request {e}'
    Clients.insert(**body.dict()).execute()
    return 200, 'ok'
