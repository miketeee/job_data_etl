from utility_operations.string_translation_operations import string_translation_operations
from first_pass_operations.match_index_operations import match_index


def create_a_set_of_uique_strings_from_job_titles(list_of_strings):
    """
    :param list_of_strings:
    :return:
    """

    all_jobs_titles = []
    unique_job_titles = set()

    for job in list_of_strings:
        job_title = job[0]
        translated_string = string_translation_operations.perform_string_translation(job_title)

        split_job_title = translated_string.split(' ')
        indices_of_length_one_removed = match_index.remove_indices_that_have_a_length_of_one(split_job_title)
        all_jobs_titles.extend(indices_of_length_one_removed)

    for word in all_jobs_titles:
        unique_job_titles.add(word)




    return unique_job_titles, all_jobs_titles


def create_set_of_unique_companies(list_of_strings):
    """

    :param list_of_strings:
    :return:
    """

    all_company_names = []
    unique_company_names = set()

    for job in list_of_strings:
        company_name = job[1]
        all_company_names.append(company_name)

    for company_name in all_company_names:
        unique_company_names.add(company_name)

    return unique_company_names, all_company_names

