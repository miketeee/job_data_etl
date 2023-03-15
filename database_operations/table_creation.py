def create_job_data_table_and_set_column_values(conn, cur):
    """

    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS job_data "
                "(job_title varchar NOT NULL, "
                "company varchar NOT NULL, "
                "location varchar NOT NULL, "
                "upload_date date NOT NULL,"
                "PRIMARY KEY (job_title, company, location, upload_date));")
    conn.commit()


def create_companies_table_and_set_column_values(conn, cur):
    """

    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS companies "
                "(company_id serial NOT NULL, "
                "company_name varchar PRIMARY KEY NOT NULL);")
    conn.commit()


def create_company_daily_job_stats_table_and_set_column_values(conn, cur):
    """

    :param conn:
    :param cur:
    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS company_daily_job_stats"
                "(company_name varchar REFERENCES companies (company_name) NOT NULL, "
                "job_count integer DEFAULT 0, "
                "job_date date);")
    conn.commit()


def create_recurring_job_title_words_table_and_set_column_values(conn, cur):
    """

    :param conn:
    :param cur:
    :return:
    """

    cur.execute("CREATE TABLE IF NOT EXISTS recurring_job_title_words"
                "(word varchar, "
                "word_daily_rank integer, "
                "word_date date, "
                "word_occurrence_rate double precision);")

    conn.commit()



