import transformation_script
from database_operations import db_connection, db_cursor, table_creation, data_insertion
from datetime_operations import datetime_operations
from set_operations import set_operations

if __name__ == '__main__':
    current_date = datetime_operations.get_todays_date_and_format_it_as_m_d_y()
    transformed_data = transformation_script.transform_csv_data('rawJobData.csv')

    unique_words_in_job_title = set_operations.create_a_set_of_uique_strings_from_job_titles(transformed_data)[0]
    unique_company_names = set_operations.create_set_of_unique_companies(transformed_data)[0]

    connection = db_connection.get_db_connection()
    cursor = db_cursor.get_db_cursor(connection)

    table_creation.create_job_data_table_and_set_column_values(connection, cursor)
    table_creation.create_companies_table_and_set_column_values(connection, cursor)
    table_creation.create_company_daily_job_stats_table_and_set_column_values(connection, cursor)
    table_creation.create_recurring_job_title_words_table_and_set_column_values(connection, cursor)

    data_insertion.insert_data_into_job_data_table(connection, cursor, transformed_data)

    db_cursor.close_db_cursor(cursor)
    db_connection.close_db_connection(connection)




