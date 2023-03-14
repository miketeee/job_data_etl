import psycopg2
from dotenv import dotenv_values


def get_db_connection():
    """

    :return:
    """

    dbname = dotenv_values()['DBNAME']
    user_name = dotenv_values()['USER']
    password = dotenv_values()['PASSWORD']
    host = dotenv_values()['HOST']
    port = dotenv_values()['PORT']

    conn = psycopg2.connect(dbname=dbname, user=user_name, password=password)

    return conn


def close_db_connection(conn):
    conn.close()

    return conn.closed
