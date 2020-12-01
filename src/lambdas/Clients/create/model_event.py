from dataclasses import dataclass
from datetime import datetime

from tools_lambda.generic_tools import (get_mty_datetime, ModelBaseEvent)


@dataclass
class BodyNewClient(ModelBaseEvent):
    names: str
    last_name: str
    telephone: str = None
    email: str = None
    group: str = None
    create_at: datetime = get_mty_datetime()
    modify_at: str = None
    create_by: str = None
    modify_by: str = None
