import sqlite3
from typing import List, Dict, Any

DB_PATH = 'instance/reservations.db'

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def insert_reservation(name: str, email: str, date: str, time: str, people: int) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservation (name, email, date, time, people)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, date, time, people))
    conn.commit()
    conn.close()

def get_all_reservations() -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservation")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def insert_order(student_name: str, student_id: str, item: str) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO 'order' (student_name, student_id, item)
        VALUES (?, ?, ?)
    """, (student_name, student_id, item))
    conn.commit()
    conn.close()

def get_all_orders() -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'order'")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# Usage examples:
# insert_reservation('John Doe', 'john@example.com', '2023-07-01', '19:00', 4)
# reservations = get_all_reservations()
# insert_order('Jane Smith', 'S12345', 'Cheese Onion Burger')
# orders = get_all_orders()
