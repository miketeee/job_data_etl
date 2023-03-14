def get_db_cursor(conn):
    """

    :return:
    """

    cur = conn.cursor()

    return cur


def close_db_cursor(cursor):
    """

    :return:
    """
    cursor.close()

    return cursor.closed