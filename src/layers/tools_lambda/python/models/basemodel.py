import os

import pandas as pd
from peewee import PostgresqlDatabase, Model
from peewee import (SelectBase, database_required)
from tools_lambda.aws import get_ssm_parameter

PROJECT = os.environ.get('PROJECT')
database = PostgresqlDatabase(get_ssm_parameter('name-database', False).get(PROJECT),
                              **get_ssm_parameter('credentials-database'))


@database_required
def get_all(self, database):
    self._cursor_wrapper = None
    try:
        return self.execute(database)[:None]
    except IndexError:
        pass


@database_required
def to_dataframe(self, database):
    self._cursor_wrapper = None
    try:
        return pd.DataFrame(self.execute(database)[:None])
    except IndexError:
        pass


setattr(SelectBase, "get_all", get_all)
setattr(SelectBase, "to_dataframe", to_dataframe)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database
