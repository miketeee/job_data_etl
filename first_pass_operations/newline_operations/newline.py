def strip_newline_char_from_end_of_string(list_of_strings_to_strip):
    """
    List of strings will be looped through and the newline \n char
    will be stripped from the end of the string.
    :param list_of_strings_to_strip:
    :return: list_of_strings_with_newline_char_stripped_away
    """

    list_of_strings_with_newline_char_stripped_away = []

    for string_to_strip in list_of_strings_to_strip:
        list_of_strings_with_newline_char_stripped_away.append(string_to_strip.strip('\n'))

    return list_of_strings_with_newline_char_stripped_away
