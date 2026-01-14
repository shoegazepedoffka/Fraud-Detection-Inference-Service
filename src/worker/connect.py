import psycopg

from app.config import DB_CONFIG

def get_connection():
    """
    Connecting to the database.
    """
    try:
        conn = psycopg.connect(**DB_CONFIG)
        return conn
    except psycopg.Error as e:
        print("Connection error:", e)
        return None

