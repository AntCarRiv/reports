import os

import pandas as pd
from peewee import PostgresqlDatabase, Model
from peewee import (SelectBase, database_required)


database = PostgresqlDatabase('reports',
                              **{'host': os.environ.get("HOST_DB"),
                                 'port': os.environ.get("PORT_DB"),
                                 'user': os.environ.get("USER_DB"),
                                 'password': os.environ.get("PASSWORD_DB")})


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
