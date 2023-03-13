def transfrom_all_to_lowercase(list_of_strings):
    """

    :param list_of_strings:
    :return:
    """

    strings_with_case_lowered = []

    for string in list_of_strings:
        strings_with_case_lowered.append(string.lower())

    return strings_with_case_lowered