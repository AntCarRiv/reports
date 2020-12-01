import json
import logging

from tools_lambda.exceptions import WebResponseError

LOGGER = logging.getLogger()


def web_response(func):
    def decorator(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
        except Exception as e:
            LOGGER.error(str(e))
            response = 500, "Internal server error"
        if not isinstance(response, tuple):
            raise WebResponseError()
        LOGGER.debug(f'Original response: {response}')
        return manage_status_code(*response)

    return decorator


def manage_status_code(status_code, response):
    response = {
        'StatusCode': status_code,
        "body": json.dumps(response)
    }
    return response
