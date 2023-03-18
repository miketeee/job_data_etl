def create_job_data_table_and_set_column_values(conn, cur):
    """

    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS job_data "
                "(id serial UNIQUE NOT NULL,"
                "job_title varchar NOT NULL, "
                "company_name varchar NOT NULL, "
                "location varchar NOT NULL, "
                "upload_date date NOT NULL,"
                "PRIMARY KEY (id, job_title, company_name, location, upload_date));")
    conn.commit()


# def create_companies_table_and_set_column_values(conn, cur):
#     """
#
#     :return:
#     """
#
#     cur.execute("CREATE TABLE IF NOT EXISTS companies "
#                 "(company_id serial NOT NULL, "
#                 "company_name varchar PRIMARY KEY NOT NULL);")
#     conn.commit()


def create_company_daily_job_stats_table_and_set_column_values(conn, cur):
    """

    :param conn:
    :param cur:
    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS company_daily_job_stats"
                "(id serial UNIQUE NOT NULL,"
                "company_name varchar NOT NULL, "
                "job_count integer DEFAULT 0, "
                "upload_date date NOT NULL,"
                "PRIMARY KEY (id, company_name, upload_date));")
    conn.commit()


def create_recurring_job_title_words_table_and_set_column_values(conn, cur):
    """

    :param conn:
    :param cur:
    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS recurring_job_title_words"
                "(word varchar NOT NULL, "
                "word_count integer DEFAULT 0, "
                "upload_date date NOT NULL,"
                "PRIMARY KEY (word, upload_date));")

    conn.commit()



