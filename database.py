import psycopg2
from psycopg2.extras import RealDictCursor, register_hstore

def get_db():
    conn = psycopg2.connect(
        dbname="",
        user="",
        password="",
        host="",
        port="",
        cursor_factory=RealDictCursor
    )
    register_hstore(conn)
    return conn
