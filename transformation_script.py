from first_pass_operations.comma_operations import commas
from first_pass_operations.newline_operations import newline
from first_pass_operations.double_quote_operations import double_quotes
from first_pass_operations.match_index_operations import match_index
from first_pass_operations.char_case_operations import char_case
from first_pass_operations.slice_operations import slice_operations
from second_pass_operations.job_data_operations import get_current_date
from second_pass_operations.job_data_operations import company, job_title, location
from utility_operations.string_translation_operations import string_translation_operations


def transform_csv_data(csv_file):

    with open(csv_file, mode='r', encoding='utf-8-sig') as f:
        csv_data = f.readlines()

    strings_to_lower_case = char_case.transfrom_all_to_lowercase(csv_data)

    commas_replaced = commas.replace_commas_from_city_state_strings_with_hypen(strings_to_lower_case)

    new_line_char_stripped_from_end = newline.strip_newline_char_from_end_of_string(commas_replaced)

    empty_indices_removed = match_index.remove_empty_indices_from_list(new_line_char_stripped_from_end)

    indices_that_only_contain_word_new_removed = match_index.remove_indices_that_contain_only_the_word_new(
        empty_indices_removed)

    jobs_starting_indices = double_quotes.detect_if_double_quote_exists_at_beggining_of_string(
        indices_that_only_contain_word_new_removed)

    strings_sliced_into_individual_lists = slice_operations.slice_list_of_jobs_into_individual_jobs(
        indices_that_only_contain_word_new_removed, jobs_starting_indices)

    jobs_with_cleaned_location = location.clean_location_data_to_show_city_only(
        strings_sliced_into_individual_lists)

    jobs_with_cleaned_company = company.remove_company_rating_from_company_name(jobs_with_cleaned_location)

    jobs_with_cleaned_title = job_title.remove_double_quote_from_beggining_of_job_title(jobs_with_cleaned_company)

    jobs_with_current_date_added = get_current_date.add_todays_date_to_job_data(jobs_with_cleaned_title)

    jobs_ready_for_loading_into_db = string_translation_operations.perform_string_translation_on_job_title(jobs_with_current_date_added)

    return jobs_ready_for_loading_into_db
