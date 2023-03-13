def clean_location_data_to_show_city_only(list_of_strings):
    """

    :param list_of_strings:
    :return: list_of_strings_with_location_cleaned
    """

    jobs_with_cleaned_location_data = []

    for job in list_of_strings:
        location = job[2].split('-')[0]
        job[2] = location

        jobs_with_cleaned_location_data.append(job)

    return jobs_with_cleaned_location_data