import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        user_id INTEGER,
        query TEXT
    )
    ''')
    conn.commit()
    conn.close()

def save_search(user_id: int, query: str):
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (user_id, query) VALUES (?, ?)", (user_id, query))
    conn.commit()
    conn.close()

def get_user_history(user_id: int):
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT query FROM history WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
