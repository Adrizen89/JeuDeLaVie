import sqlite3

def create_connection():
    """ Crée une connexion à la base de données SQLite. """
    conn = sqlite3.connect('game_of_life.db')
    return conn

def initialize_db():
    """ Initialise la base de données avec les tables nécessaires. """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()
