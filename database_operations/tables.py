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
                "(company_id serial REFERENCES companies (company_id),"
                "day_zero_job_count integer DEFAULT 0);")
    conn.commit()


def create_column_for_todays_date_in_company_stats_table(conn, cur, current_date):
    """

    :param conn:
    :param cur:
    :param current_date:
    :return:
    """

    cur.execute(f"ALTER TABLE company_daily_job_stats ADD COLUMN IF NOT EXISTS {current_date} integer DEFAULT 0")
    conn.commit()


