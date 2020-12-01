from models.models import Clients
from tools_lambda.decorators import web_response
from tools_lambda.generic_tools import (get_logger, get_body)

from .model_event import BodyDeleteClient

LOGGER = get_logger()


@web_response
def lambda_handler(event, context):
    try:
        body = BodyDeleteClient(**get_body(event))
    except TypeError as e:
        LOGGER.error(str(e))
        return 400, 'Bad request'
    result = Clients.delete().where(Clients.id == body.client_id).execute()
    if not result:
        LOGGER.warning('Any element was deleted')
        return 204, ''
    return 200, f'Client with id {body.client_id} was deleted'
