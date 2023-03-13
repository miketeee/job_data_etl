def remove_double_quote_from_beggining_of_job_title(list_of_strings):
    """

    :return:
    """

    jobs_with_double_quote_removed_from_beggining_of_title = []

    for job in list_of_strings:
        job[0] = job[0].replace('"', '')

        jobs_with_double_quote_removed_from_beggining_of_title.append(job)

    return jobs_with_double_quote_removed_from_beggining_of_title