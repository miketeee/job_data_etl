from first_pass_operations.char_case_operations import char_case


def test_lowering_case_of_string():
    """

    :return:
    """

    inital_strings = ['Hello', 'WORLD', "bUilDInG"]

    expected_strings = ['hello', 'world', 'building']

    strings_to_lower_case = char_case.transfrom_all_to_lowercase(inital_strings)

    assert expected_strings == strings_to_lower_case