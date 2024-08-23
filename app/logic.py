import mysql.connector
import os

# MySQL configuration
write_db_config = {
    'user': os.getenv('WRITE_DB_USER'),
    'password': os.getenv('WRITE_DB_PASSWORD'),
    'host': os.getenv('WRITE_DB_HOST'),
    'database': os.getenv('DB_NAME')
}

read_db_config = {
    'user': os.getenv('READ_DB_USER'),
    'password': os.getenv('READ_DB_PASSWORD'),
    'host': os.getenv('READ_DB_HOST'),
    'database': os.getenv('DB_NAME')
}

def get_db_connection(config):
    return mysql.connector.connect(**config)

def get_users():
    conn = get_db_connection(read_db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def add_user_to_db(name, email):
    conn = get_db_connection(write_db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
