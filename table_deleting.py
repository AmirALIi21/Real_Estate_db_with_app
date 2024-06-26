import psycopg2
from psycopg2 import sql

def connect_db():
    return psycopg2.connect(
        host='localhost',
        dbname='your_db_name',
        user='postgres',
        password='your_pass',
        port=5432
    )

def drop_all_tables():
    conn = connect_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)

        tables = cur.fetchall()


        cur.execute("SET session_replication_role = 'replica';")
        for table in tables:
            cur.execute(sql.SQL("DROP TABLE IF EXISTS {} CASCADE;").format(sql.Identifier(table[0])))

        cur.execute("SET session_replication_role = 'origin';")

        conn.commit()
        print("All tables dropped successfully.")

    except psycopg2.Error as e:
        print(f"Database error: {e}")

    finally:
        cur.close()
        conn.close()


drop_all_tables()
