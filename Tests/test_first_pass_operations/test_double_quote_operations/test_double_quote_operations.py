from first_pass_operations.double_quote_operations import double_quotes


def test_detecting_if_string_ends_with_a_double_quote():

    strings_to_check = [
        '"Plummer',
        'Plummers R\' US',
        'new"',
        'just posted"'
    ]

    found_strings = double_quotes.detect_if_double_quote_exists_at_end_of_string(strings_to_check)

    assert [2, 3] == found_strings


def test_detecting_if_string_begins_with_a_double_quote():

    strings_to_check = [
        '"Plummer',
        '"Plummers R\' US',
        'new',
        'just posted"'
    ]

    found_strings = double_quotes.detect_if_double_quote_exists_at_beggining_of_string(strings_to_check)

    assert [0, 1] == found_strings
