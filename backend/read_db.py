import sqlite3

def print_table_contents(db_path, table_name, limit=5):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit};")
        rows = cursor.fetchall()
        print(f"Contents of table '{table_name}':")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    db_path = "instance/reservations.db"
    print_table_contents(db_path, "Reservation")
    print()
    print_table_contents(db_path, "Order")
