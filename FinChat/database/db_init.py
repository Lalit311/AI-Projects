from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "finance.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"


def initialize_database():

    conn = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r") as f:
        schema = f.read()

    conn.executescript(schema)

    conn.commit()
    conn.close()

    print(f"Database created successfully at:\n{DB_PATH}")


if __name__ == "__main__":
    initialize_database()