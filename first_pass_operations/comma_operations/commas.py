def replace_commas_from_city_state_strings_with_hypen(list_of_strings):
    """
    The scraped job data for the majority of jobs contains a city and state (Dallas, Tx).
    The commas will be removed and replace with a hypen because the initial job data is
    not formated and will later be split on commas. Therefore we do not want the program
    to split on the city, state section.
    :param list_of_strings:
    :return: string_with_comma_replaced_by_hypen
    """

    list_of_strings_with_commas_replaced_with_hypens = []
    for string_to_check in list_of_strings:
        list_of_strings_with_commas_replaced_with_hypens.append(string_to_check.replace(',', '-').strip())

    return list_of_strings_with_commas_replaced_with_hypens
