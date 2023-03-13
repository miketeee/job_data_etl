
def slice_list_of_jobs_into_individual_jobs(list_of_strings, job_data_starting_indices_list):
    """
    Using the list of nums that indicate the starting index for each job,
    slice
    :param job_data_starting_indices_list:
    :param list_of_strings:
    :return: jobs_sliced_into_individuals
    """

    jobs_sliced_into_individuals = []

    for starting_index in job_data_starting_indices_list:
        if not list_of_strings[starting_index + 2]:
            pass
        else:
            job_title = list_of_strings[starting_index]
            company = list_of_strings[starting_index + 1]
            location = list_of_strings[starting_index + 2]

            sliced_job = [job_title,company, location]

            jobs_sliced_into_individuals.append(sliced_job)

    return jobs_sliced_into_individuals
