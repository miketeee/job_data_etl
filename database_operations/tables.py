def create_job_data_table_and_set_column_values(conn, cur):
    """

    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS job_data "
                "(id serial PRIMARY KEY NOT NULL, "
                "job_title varchar NOT NULL, "
                "company varchar NOT NULL, "
                "upload_date date NOT NULL);")
    conn.commit()


def create_companies_table_and_set_column_values(conn, cur):
    """

    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS companies "
                "(company_id serial PRIMARY KEY NOT NULL, "
                "company_name varchar NOT NULL);")
    conn.commit()


def create_company_daily_job_stats_table_and_set_column_values(conn, cur):
    """

    :param conn:
    :param cur:
    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS company_daily_job_stats"
                "(company_id serial REFERENCES companies (company_id), "
                "job_count integer DEFAULT 0, "
                "job_date date);")
    conn.commit()





