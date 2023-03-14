import transformation_script
from database_operations import db_connection, db_cursor
import psycopg2

if __name__ == '__main__':
    transformed_data = transformation_script.transform_csv_data('rawJobData.csv')

    connection = db_connection.get_db_connection()
    cursor = db_cursor.get_db_cursor(connection)

    db_cursor.close_db_cursor(cursor)
    db_connection.close_db_connection(connection)




