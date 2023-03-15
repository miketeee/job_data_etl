import re


def remove_company_rating_from_company_name(list_of_strings):
    """

    :param list_of_strings:
    :return:
    """

    jobs_with_company_rating_removed = []

    re_pattern1 = re.compile(r'[a-z |\.][0-9]')

    for job in list_of_strings:
        company = job[1]
        if re_pattern1.search(company) is None:
            jobs_with_company_rating_removed.append(job)
        else:
            match = re_pattern1.search(company)
            index_to_slice_on = match.start() + 1
            job[1] = company[:index_to_slice_on]
            jobs_with_company_rating_removed.append(job)

    return jobs_with_company_rating_removed
