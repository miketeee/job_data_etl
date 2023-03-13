from datetime_operations import datetime_operations

def add_todays_date_to_job_data(list_of_strings):
    """

    :param list_of_strings:
    :return:
    """

    list_of_jobs_with_todays_date_added = []

    for job in list_of_strings:
        job.append(f'{datetime_operations.get_todays_date_and_format_it_as_m_d_y()}')
        list_of_jobs_with_todays_date_added.append(job)

    return list_of_jobs_with_todays_date_added