import csv

def insert_data_into_job_data_table(conn, cur, data_to_insert):
    """

    :param conn:
    :param cur:
    :return:
    """

    for job in data_to_insert:
        job_title, company, location, job_date = job[0], job[1], job[2], job[3]

        cur.execute("INSERT INTO job_data (job_title, company_name, location, upload_date) "
                       "VALUES (%s, %s, %s, %s) ON CONFLICT (id, job_title, company_name, location, upload_date) DO NOTHING",
                       (job_title, company, location, job_date))
        conn.commit()


def insert_data_into_companies_table(conn, cur, data_to_insert, upload_date):
    """

    :param conn:
    :param cur:
    :param data_to_insert:
    :return:
    """

    for key in data_to_insert.keys():
        company_name = key
        company_job_count = data_to_insert[company_name]

        cur.execute("INSERT INTO company_daily_job_stats (company_name, job_count, upload_date) "
                    "VALUES (%s, %s, %s) ON CONFLICT (id, company_name, upload_date) DO NOTHING",
                    (company_name, company_job_count, upload_date))
        conn.commit()


def insert_data_into_recurring_job_title_words(conn, cur, data_to_insert, upload_date):
    """

    :param conn:
    :param cur:
    :param data_to_insert:
    :param upload_date:
    :return:
    """

    for key in data_to_insert.keys():
        word = key
        word_count = data_to_insert[word]

        cur.execute("INSERT INTO recurring_job_title_words (word, word_count, upload_date) "
                    "VALUES (%s, %s, %s) ON CONFLICT (word, upload_date) DO NOTHING",
                    (word, word_count, upload_date))
        conn.commit()