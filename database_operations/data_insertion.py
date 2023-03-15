def insert_data_into_job_data_table(conn, cur, data_to_insert):
    """

    :param conn:
    :param cur:
    :return:
    """

    for job in data_to_insert:
        job_title, company, location, job_date = job[0], job[1], job[2], job[3]

        job_id = f"{job_title}{company}{location}{job_date}"


        cur.execute("INSERT INTO job_data (job_title, company, location, upload_date) "
                       "VALUES (%s, %s, %s, %s) ON CONFLICT (job_title, company, location, upload_date) DO NOTHING",
                       (job_title, company, location, job_date))
        conn.commit()
