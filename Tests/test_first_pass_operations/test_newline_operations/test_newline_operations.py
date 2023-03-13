from first_pass_operations.newline_operations import newline


def test_stripping_newline_char_from_end_of_string():
    """
    Each job's data is split onto multiple lines in the initial file.
    The newline \n is not needed and needs to be removed.
    :return: 
    """
    
    initial_list_of_string_with_newline_char_stripped_from_the_end = [
        '\n',
        'tower worker tier 1\n',
        'Tiny Town, Utah 65894\n'
    ]
    
    expected_list_of_strings_with_newline_char_stripped_from_the_end = [
        '',
        'tower worker tier 1',
        'Tiny Town, Utah 65894'
    ]
    
    list_of_strings_with_newline_char_stripped_from_the_end = newline.strip_newline_char_from_end_of_string(initial_list_of_string_with_newline_char_stripped_from_the_end)

    assert list_of_strings_with_newline_char_stripped_from_the_end == expected_list_of_strings_with_newline_char_stripped_from_the_end