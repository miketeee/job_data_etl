from second_pass_operations.job_data_operations import search_date
from second_pass_operations.job_data_operations import company, job_title, location
from datetime_operations import datetime_operations


def test_removing_location_data_except_for_city():

    initial_strings = [
        ['"attendance clerk - high school', 'arlington independent school district3.8', 'arlington- tx 76013'],
        ['"car wash attendant/detailer', 'audi grapevine2.7', 'grapevine- tx 76051'],
        ['"customer service representative sales (wfh - work from home)', 'at&t3.7', 'remote in dallas- tx']
    ]

    expected_strings = [
        ['"attendance clerk - high school', 'arlington independent school district3.8', 'arlington'],
        ['"car wash attendant/detailer', 'audi grapevine2.7', 'grapevine'],
        ['"customer service representative sales (wfh - work from home)', 'at&t3.7', 'remote in dallas']
    ]

    cleaned_location_strings = location.clean_location_data_to_show_city_only(initial_strings)

    assert expected_strings == cleaned_location_strings


def test_removing_company_rating_from_company_name():

    initial_strings = [
        ['"attendance clerk - high school', 'arlington independent school district3.8', 'arlington'],
        ['"car wash attendant/detailer', 'audi grapevine2.7', 'grapevine'],
        ['"customer service representative sales (wfh - work from home)', 'at&t3.7', 'remote in dallas']
    ]

    expected_strings = [
        ['"attendance clerk - high school', 'arlington independent school district', 'arlington'],
        ['"car wash attendant/detailer', 'audi grapevine', 'grapevine'],
        ['"customer service representative sales (wfh - work from home)', 'at&t', 'remote in dallas']
    ]

    strings_with_company_rating_removed = company.remove_company_rating_from_company_name(initial_strings)

    assert expected_strings == strings_with_company_rating_removed

def test_removing_double_quote_from_beggining_of_job_title():

    initial_strings = [
        ['"attendance clerk - high school', 'arlington independent school district', 'arlington'],
        ['"car wash attendant/detailer', 'audi grapevine', 'grapevine'],
        ['"customer service representative sales (wfh - work from home)', 'at&t', 'remote in dallas']
    ]

    expected_strings = [
        ['attendance clerk - high school', 'arlington independent school district', 'arlington'],
        ['car wash attendant/detailer', 'audi grapevine', 'grapevine'],
        ['customer service representative sales (wfh - work from home)', 'at&t', 'remote in dallas']
    ]

    strings_with_double_quote_removed_from_beggining = job_title.remove_double_quote_from_beggining_of_job_title(initial_strings)

    assert expected_strings == strings_with_double_quote_removed_from_beggining


def test_adding_todays_date_to_job_data():
    todays_date = datetime_operations.get_todays_date_and_format_it_as_m_d_y()

    initial_strings = [
        ['attendance clerk - high school', 'arlington independent school district', 'arlington'],
        ['car wash attendant/detailer', 'audi grapevine', 'grapevine'],
        ['customer service representative sales (wfh - work from home)', 'at&t', 'remote in dallas']
    ]

    expected_strings = [
        ['attendance clerk - high school', 'arlington independent school district', 'arlington', f'{todays_date}'],
        ['car wash attendant/detailer', 'audi grapevine', 'grapevine', f'{todays_date}'],
        ['customer service representative sales (wfh - work from home)', 'at&t', 'remote in dallas', f'{todays_date}']
    ]

    strings_with_todays_date_added = search_date.add_todays_date_to_job_data(initial_strings)

    assert expected_strings == strings_with_todays_date_added
