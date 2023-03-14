import psycopg2
from database_operations import db_connection, db_cursor
from Tests.testing_fixtures.testing_fixtures import connection, cursor


def test_getting_database_connection_object(connection):

    if isinstance(connection, psycopg2.extensions.connection):
        connection = True

    assert connection is True


def test_that_db_connection_is_closed(connection):

    connection_status = db_connection.close_db_connection(connection)

    assert connection_status is 1


def test_that_cursor_is_not_closed(cursor):

    cur_status = cursor.closed

    assert cur_status is False


def test_that_cursor_is_closed(cursor):

    cursor_status = db_cursor.close_db_cursor(cursor)

    assert cursor_status is True


