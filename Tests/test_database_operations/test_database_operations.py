import psycopg2
from database_operations import db_connection


def test_getting_database_connection_object():
    connection_obj = db_connection.get_db_connection()

    assert isinstance(connection_obj, psycopg2.extensions.connection) == True