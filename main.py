import transformation_script
from database_operations import db_connection, db_cursor, table_creation, data_insertion
from utility_operations.datetime_operations import datetime_operations
from utility_operations.set_operations import set_operations
from utility_operations.dict_operations import dict_operations

if __name__ == '__main__':
    current_date = datetime_operations.get_todays_date_and_format_it_as_m_d_y()

    # Csv data prep
    transformed_data = transformation_script.transform_csv_data('csvfiles/jobData.csv')

    unique_and_all_words_in_job_title = set_operations.create_a_set_of_uique_strings_from_job_titles(transformed_data)
    unique_and_all_company_names = set_operations.create_set_of_unique_companies(transformed_data)

    all_words_in_job_titles = unique_and_all_words_in_job_title[1]
    all_company_names = unique_and_all_company_names[1]

    companies_frequency = dict_operations.create_dict_of_frequency_of_string(all_company_names)
    job_title_words_frequency = dict_operations.create_dict_of_frequency_of_string(all_words_in_job_titles)

    # Connect to database
    connection = db_connection.get_db_connection()
    cursor = db_cursor.get_db_cursor(connection)

    # Create tables if they do not exist
    table_creation.create_job_data_table_and_set_column_values(connection, cursor)
    table_creation.create_company_daily_job_stats_table_and_set_column_values(connection, cursor)
    table_creation.create_recurring_job_title_words_table_and_set_column_values(connection, cursor)

    # Insert transformed csv data into tables
    data_insertion.insert_data_into_job_data_table(connection, cursor, transformed_data)
    data_insertion.insert_data_into_companies_table(connection, cursor, companies_frequency, current_date)
    data_insertion.insert_data_into_recurring_job_title_words(connection, cursor, job_title_words_frequency, current_date)



    # Close database connection and cursor
    db_cursor.close_db_cursor(cursor)
    db_connection.close_db_connection(connection)




