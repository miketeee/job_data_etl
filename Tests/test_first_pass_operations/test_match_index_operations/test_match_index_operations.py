from first_pass_operations.match_index_operations import match_index


def test_deleting_empty_indices_from_list():
    """
    Tests deleting empty indices from list of non-empty and empty-strings
    :return: 
    """
    
    initial_list_of_strings = [' ', '', 'job', 'city ', '   ', "", " ", "   "]
    
    expected_list_of_strings = ['job', 'city ']
    
    list_of_strings_with_empty_indices_removed = match_index.remove_empty_indices_from_list(initial_list_of_strings)
    
    assert expected_list_of_strings == list_of_strings_with_empty_indices_removed


def test_deleting_indices_that_only_contain_the_word_new_from_list():
    """

    :return:
    """

    initial_list_of_strings = ['new', 'old', 'run', 'kinda new', 'slightlynew', 'new', 'jump']

    expected_list_of_strings = ['old', 'run', 'kinda new', 'slightlynew', 'jump']

    list_of_strings_without_indices_that_only_contain_the_word_new = match_index.\
        remove_indices_that_contain_only_the_word_new(initial_list_of_strings)

    assert expected_list_of_strings == list_of_strings_without_indices_that_only_contain_the_word_new