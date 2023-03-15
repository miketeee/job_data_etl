def create_dict_of_frequency_of_string(list_of_strings):
    """

    :param list_of_strings:
    :param set_of_strings:
    :return: dict_of_string_frequencies
    """

    string_frequency_dict = {}

    for string in list_of_strings:
        if string not in string_frequency_dict.keys() and string != '':
            string_frequency_dict.update({string: 1})
        elif string != '':
            string_frequency_dict.update({string: string_frequency_dict[string] + 1})

    return string_frequency_dict