from utility_operations.dict_operations import dict_operations


def test_creating_dict_of_string_frequencies():
    initial_strings = ['aa', 'bb', 'cc', 'dd', 'aa', 'aa', 'bb']

    expected_dict = {'aa': 3, 'bb': 2, 'cc': 1, 'dd': 1}

    assert expected_dict == dict_operations.create_dict_of_frequency_of_string(initial_strings)
