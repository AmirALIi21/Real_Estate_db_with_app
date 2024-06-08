import psycopg2
from psycopg2 import sql

# Function to connect to the PostgreSQL database
def connect_db():
    return psycopg2.connect(
        host='localhost',
        dbname='real_estate_v01',
        user='postgres',
        password='13801380',
        port=5432
    )

# Function to drop all tables in the database
def drop_all_tables():
    conn = connect_db()
    cur = conn.cursor()

    try:
        # Fetch all table names in the current database schema
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)

        tables = cur.fetchall()

        # Disable foreign key checks
        cur.execute("SET session_replication_role = 'replica';")

        # Drop each table
        for table in tables:
            cur.execute(sql.SQL("DROP TABLE IF EXISTS {} CASCADE;").format(sql.Identifier(table[0])))

        # Enable foreign key checks
        cur.execute("SET session_replication_role = 'origin';")

        conn.commit()
        print("All tables dropped successfully.")

    except psycopg2.Error as e:
        print(f"Database error: {e}")

    finally:
        cur.close()
        conn.close()

# Run the function to drop all tables
drop_all_tables()
