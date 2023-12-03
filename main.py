from dotenv import load_dotenv, find_dotenv
import mysql.connector
import os

def connect_database():
    # find .env automagically by walking up directories until it's found
    dotenv_path = find_dotenv()
    
    # load up the entries as environment variables
    load_dotenv(dotenv_path)

    DB_URL = os.environ.get("DB_URL")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    
    if DB_URL and DB_USER and DB_PASSWORD:
        # Creating connection object
        try:
            db_conn = mysql.connector.connect(
                host=DB_URL,
                user=DB_USER,
                password=DB_PASSWORD
            )
            print('Successfully connected to the database...')
            return db_conn
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            return None
    else:
        print("Database configuration missing in environment variables.")
        return None

if __name__ == '__main__':
    # Create connection object
    db_conn = connect_database()
