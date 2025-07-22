import sqlite3
import sys

def initialize_database():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 category TEXT, 
                 amount FLOAT, 
                 date TEXT)''')
    conn.commit()
    return conn, c

def add_transaction(category, amount, date, conn, c):
    if not category or amount <= 0:
        raise ValueError("Invalid category or amount")
    c.execute('INSERT INTO transactions (category, amount, date) VALUES (?, ?, ?)', 
             (category, amount, date))
    conn.commit()
    print(f"Added transaction: {category}, ${amount:.2f}, {date}")

def view_summary(c):
    c.execute('SELECT category, SUM(amount) AS total FROM transactions GROUP BY category')
    print("\nTransaction Summary:")
    print("----------------------")
    for row in c.fetchall():
        print(f"{row[0]}: ${row[1]:.2f}")

def main():
    try:
        conn, c = initialize_database()
        sample_transactions = [
            ('Salary', 1500.0, '2025-07-22'),
            ('Groceries', 75.0, '2025-07-22'),
            ('Utilities', 100.0, '2025-07-22'),
            ('Rent', 800.0, '2025-07-22')
        ]
        for transaction in sample_transactions:
            add_transaction(*transaction, conn, c)
        view_summary(c)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
