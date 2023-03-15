from dict_operations import dict_operations


def test_creating_dict_of_string_frequencies():
    initial_strings = ['a', 'b', 'c', 'd', 'a', 'a', 'b']

    expected_dict = {'a': 3, 'b': 2, 'c': 1, 'd': 1}

    assert expected_dict == dict_operations.create_dict_of_frequency_of_string(initial_strings)
