from first_pass_operations.slice_operations import slice_operations


def test_slicing_list_of_jobs_into_individual_jobs():
    """

    :param list_of_strings:
    :return: list_of_individual_jobs
    """
    list_of_starting_index_positions_for_each_job = [0, 4, 8]

    initial_list_strings = ['Plummer', 'Plummers inc', 'Dallas- tx 76543', '$25 an hour',
                            'Builder', 'Builders inc', 'Houston- tx 77443', '$28 an hour',
                            'Eater', 'Eaters inc', 'Dallas- tx 84543', '$70k'
                            ]

    expected_list_of_strings = [['Plummer', 'Plummers inc', 'Dallas- tx 76543'],
                                ['Builder', 'Builders inc', 'Houston- tx 77443'],
                                ['Eater', 'Eaters inc', 'Dallas- tx 84543']
                                ]

    sliced_job_data = slice_operations.\
        slice_list_of_jobs_into_individual_jobs(initial_list_strings,list_of_starting_index_positions_for_each_job)

    assert expected_list_of_strings == sliced_job_data
