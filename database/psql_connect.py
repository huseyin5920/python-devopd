# database/psql_connect.py
import psycopg2
from psycopg2.extras import RealDictCursor

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="citizix_db",
            user="citizix_user",
            password="S3cret",
            host="localhost",  # Eğer Docker kullanıyorsanız 'postgres' olabilir
            port="5432"
        )
        return connection
    except Exception as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

def execute_query(query, params=None):
    connection = connect_to_db()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, params)
        connection.commit()
        result = None
        if cursor.description:  # Eğer sorgu bir sonuç döndürüyorsa (SELECT gibi)
            result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except Exception as error:
        print("Error executing query:", error)
        return None

def insert_server_info(server_name, server_ip, server_port, server_type, server_os_name):
    query = """
    INSERT INTO server_info (server_name, server_ip, server_port, server_type, server_os_name) 
    VALUES (%s, %s, %s, %s, %s)
    """
    params = (server_name, server_ip, server_port, server_type, server_os_name)
    execute_query(query, params)