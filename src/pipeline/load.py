import psycopg2
from src.logger import logger

def load_data(data):
    logger.info("Load: подключение к PostgreSQL")

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="stage1",
        user="admin",
        password="pass123"
    )

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        adult BOOLEAN
    );
    """)

    for row in data:
        cur.execute("""
            INSERT INTO users (id, name, age, adult)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET
                name = EXCLUDED.name,
                age = EXCLUDED.age,
                adult = EXCLUDED.adult;
        """, (row["id"], row["name"], row["age"], row["adult"]))

    conn.commit()
    cur.close()
    conn.close()

    logger.info("Load: данные успешно загружены")
