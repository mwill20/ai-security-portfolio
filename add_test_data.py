import sqlite3
import os
from datetime import datetime, timedelta

def add_test_data():
    db_path = os.path.join('instance', 'portfolio.db')
    
    # Sample test data
    test_entries = [
        ("Alice", "I love this website! It's amazing!", "positive"),
        ("Bob", "This is just okay, not great.", "neutral"),
        ("Charlie", "I'm not sure how I feel about this.", "neutral"),
        ("David", "This website is terrible and I hate it!", "negative"),
        ("Eve", "This is a test for SQL injection: ' OR '1'='1", "neutral"),
        ("Mallory", "Another test: '; DROP TABLE guestbook; --", "negative")
    ]
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Add test entries with different timestamps
    for i, (name, message, sentiment) in enumerate(test_entries):
        timestamp = (datetime.now() - timedelta(hours=i)).strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            'INSERT INTO guestbook (name, message, timestamp, sentiment) VALUES (?, ?, ?, ?)',
            (name, message, timestamp, sentiment)
        )
    
    conn.commit()
    conn.close()
    print(f"✅ Added {len(test_entries)} test entries to the guestbook")

if __name__ == "__main__":
    add_test_data()
