import transformation_script
from database_operations import db_connection, db_cursor, tables
from datetime_operations import datetime_operations
import psycopg2

if __name__ == '__main__':
    current_date = datetime_operations.get_todays_date_and_format_it_as_m_d_y()
    transformed_data = transformation_script.transform_csv_data('rawJobData.csv')

    connection = db_connection.get_db_connection()
    cursor = db_cursor.get_db_cursor(connection)

    tables.create_job_data_table_and_set_column_values(connection, cursor)
    tables.create_companies_table_and_set_column_values(connection, cursor)
    tables.create_company_daily_job_stats_table_and_set_column_values(connection, cursor)
    tables.create_column_for_todays_date_in_company_stats_table(connection, cursor, datetime_operations.get_todays_date_and_format_it_as_m_d_y())





    db_cursor.close_db_cursor(cursor)
    db_connection.close_db_connection(connection)




