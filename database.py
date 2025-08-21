import psycopg2
from psycopg2.extras import RealDictCursor, register_hstore

def get_db():
    conn = psycopg2.connect(
        dbname="nominatim_17_4m",
        user="postgres",
        password="imarg@2025",
        host="10.10.6.252",
        port="7051",
        cursor_factory=RealDictCursor
    )
    register_hstore(conn)
    return conn
