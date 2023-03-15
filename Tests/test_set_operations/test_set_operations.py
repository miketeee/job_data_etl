from set_operations import set_operations


def test_creating_a_set_from_a_list_of_strings():

    initial_list_of_strings = [
        ['warehouse worker $19-$24 +$4-000 retention bonus +$3-000 childcare yearly', 'albertsons/ tom thumb dc',
         'roanoke', '03/14/23'],
        ['early childhood teacher (infants-pre-k)', 'the goddard school - frisco- tx', 'frisco', '03/14/23'],
        ['building based sub - work everyday!', 'ess education', 'dallas', '03/14/23']
    ]

    expected_strings = {'warehouse', 'worker', 'retention', 'bonus', 'childcare', 'yearly',
         'early', 'childhood', 'teacher', 'infants', 'pre', 'building', 'based', 'sub', 'work', 'everyday'}

    assert expected_strings == set_operations.create_a_set_of_uique_strings_from_job_titles(initial_list_of_strings)[0]