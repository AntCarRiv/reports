import functools

import peewee


def transaction_for_test(database=None):
    """
    Decorator
    use:
        @transaction_for_test(database=database)
        def test_lambda_handler(self):
            "some logic"
            pass
    Create a transaction which wraps your tests in such a way that when the unit test ends, the database
    remains in the initial state when the test was not yet executed
    Args:
        database: a connection to database

    """

    def decorator(func):
        if not isinstance(database, peewee.PostgresqlDatabase):
            raise ValueError('Error')
        if database.is_closed():
            database.connect()

        @functools.wraps(func)
        def decorator_nest(self, *args, **kwargs):
            with database.transaction() as t:
                result = func(self, *args, **kwargs)
                t.rollback()
                return result

        database.close()
        return decorator_nest

    return decorator
