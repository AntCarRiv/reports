from dataclasses import dataclass
from tools_lambda.generic_tools import ModelBaseEvent


@dataclass
class BodyDeleteClient(ModelBaseEvent):
    client_id: int
