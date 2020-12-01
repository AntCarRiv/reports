import datetime
import json
import logging
from dataclasses import dataclass, asdict
from decimal import Decimal

import pytz


def get_status_code(result: dict) -> int:
    """
    Find the status code in the lambdas response
    :param result: Any lambda response
    :return: a status code
    """
    return result.get('StatusCode')


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger


def get_body(event):
    """
    Get the body from a request event
    :param event:
    :return:
    """
    if isinstance(event, str):
        event = json.loads(event)
    body = event.get('body')
    if isinstance(body, str):
        body = json.loads(body)
    return body


def get_mty_datetime():
    mty = pytz.timezone('America/Monterrey')
    return datetime.datetime.now(tz=mty)


def cast_default(o):
    """
    Cast all date time and Decimals objects in a dict
    :param o:
    :return:
    """
    if isinstance(o, (datetime.date, datetime.time)):
        o = o.isoformat()
    if isinstance(o, Decimal):
        o = cast_number(o)
    return o


def cast_number(number: (str, Decimal)) -> (int, float):
    """
    Cast any string or Decimal object to float or int
    :param number: Any number with data type Decimal or int
    :return: An int or float object
    """
    if isinstance(number, str):
        if number.isnumeric():
            return int(number)
        else:
            try:
                return float(number)
            except ValueError:
                try:
                    return float(number.replace(',', ''))
                except ValueError:
                    raise ValueError("The value not is int o float")
    elif isinstance(number, Decimal):
        return cast_number(str(number))
    elif isinstance(number, (float, int)):
        return number


def get_query_params(event, default=None):
    """
    get event qqueryStringParameters if lambda has proxy lambda integration in api gateway
    Args:
        event: The event received from the invocation via api gateway
        default:
    Returns: the value for the queryStringParameters if this exist else None
    """
    if isinstance(event, str):
        event = json.loads(event)
    return event.get('queryStringParameters', default)


@dataclass
class ModelBaseEvent:
    def dict(self):
        return asdict(self)

    def json(self):
        return json.dumps(asdict(self), default=cast_default, ensure_ascii=False)
