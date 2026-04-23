import sqlite3
import os

DB_NAME = "ett_tickets.db"

def init_db():
    db_exists = os.path.exists(DB_NAME)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT UNIQUE,
            date TEXT,
            address TEXT,
            street TEXT,
            city TEXT,
            state TEXT,
            zip TEXT,
            status TEXT,
            assignee TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

    if db_exists:
        print(f"Database '{DB_NAME}' already exists — skipping initialization.")
    else:
        print(f"Database '{DB_NAME}' created successfully.")

if __name__ == "__main__":
    init_db()


# pyid
# assignedtoname
# problemdescription
# pxcreatedatetime
# intent
# subintent
# pxupdateoperator
# ticketstatus
# fulladdress
# House Number
# Pre-directional
# Street Name
# Street Types
# Post-directional
# Unit Designators
# City
# State
# Zip 
