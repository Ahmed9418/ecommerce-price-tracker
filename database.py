# database.py
import sqlite3
from datetime import datetime

DB_NAME = "price_tracker.db"

def init_db():
    """Initializes the SQLite database and creates necessary tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Table to store the items we are tracking
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT UNIQUE NOT NULL,
            target_price REAL NOT NULL
        )
    ''')
    
    # Table to store the daily price history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            price REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def add_product(name: str, url: str, target_price: float):
    """Adds a new product to track, ignoring if the URL already exists."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO products (name, url, target_price) VALUES (?, ?, ?)", 
                       (name, url, target_price))
        conn.commit()
    except sqlite3.IntegrityError:
        pass # Product URL already exists
    finally:
        conn.close()

def log_price(product_id: int, price: float):
    """Saves the scraped price to the history table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO price_history (product_id, price) VALUES (?, ?)", 
                   (product_id, price))
    conn.commit()
    conn.close()

def get_all_products():
    """Retrieves all tracked products."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, url, target_price FROM products")
    products = cursor.fetchall()
    conn.close()
    return products