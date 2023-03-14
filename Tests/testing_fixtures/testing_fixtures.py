import pytest
from database_operations import db_connection, db_cursor


@pytest.fixture
def connection(scope="function"):
    conn = db_connection.get_db_connection()
    return conn


@pytest.fixture
def cursor(connection, scope="function"):
    cur = db_cursor.get_db_cursor(connection)
    return cur
