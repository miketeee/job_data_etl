def remove_empty_indices_from_list(list_of_strings):
    """
    Remove empty indices from input list and return list of where every
    index has a value that is not an empty string.
    :param list_of_strings:
    :return:
    """

    list_without_empty_indices = []

    for string in list_of_strings:
        if len(string.strip()) > 0:
            list_without_empty_indices.append(string)
    return list_without_empty_indices


def remove_indices_that_contain_only_the_word_new(list_of_strings):
    """

    :param list_of_strings:
    :return:
    """

    list_with_indices_that_only_contain_the_word_new = []

    for string in list_of_strings:
        if string != 'new':
            list_with_indices_that_only_contain_the_word_new.append(string)

    return list_with_indices_that_only_contain_the_word_new
