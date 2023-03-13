from first_pass_operations.comma_operations import commas


class CommaOperationsTests():
    def test_commas_replaced_with_hyphens(self):
        initial_strings = ['dallas, tx 75032', 'irving, tx 76054', 'houston, tx 70032']
        expected_strings = ['dallas- tx 75032', 'irving- tx 76054', 'houston- tx 70032']

        returned_string = commas.replace_commas_from_city_state_strings_with_hypen(initial_strings)
        assert returned_string == expected_strings