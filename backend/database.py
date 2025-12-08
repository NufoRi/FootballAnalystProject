import sqlite3

DB_NAME = "football.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_database():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT,
            logo TEXT
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            team_id INTEGER,
            name TEXT,
            position TEXT,
            age INTEGER,
            FOREIGN KEY(team_id) REFERENCES teams(id)
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY,
            home_team INTEGER,
            away_team INTEGER,
            date TEXT,
            status TEXT,
            home_goals INTEGER,
            away_goals INTEGER
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            match_id INTEGER,
            note TEXT,
            rating INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
