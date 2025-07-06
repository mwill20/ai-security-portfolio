import sqlite3
import os

def check_database():
    # Direct path to the database file
    db_path = os.path.join('instance', 'portfolio.db')
    
    print("🔍 Checking Guestbook Database")
    print("="*50)
    print(f"📂 Looking for database at: {os.path.abspath(db_path)}")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("\n❌ Database not found!")
        print("   Run this command to create it: flask init-db")
        return
    
    print("✅ Found database file")
    
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if guestbook table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='guestbook';")
        if not cursor.fetchone():
            print("\n❌ The 'guestbook' table doesn't exist.")
            print("   Run 'flask init-db' to create it.")
            return
        
        print("✅ Found guestbook table")
        
        # Count entries
        cursor.execute("SELECT COUNT(*) FROM guestbook;")
        count = cursor.fetchone()[0]
        print(f"\n📊 Found {count} entries in the guestbook")
        
        # Show table structure
        print("\n📋 Table structure:")
        cursor.execute("PRAGMA table_info(guestbook);")
        for col in cursor.fetchall():
            print(f"   - {col[1]} ({col[2]})")
        
        # Show sample entries if any exist
        if count > 0:
            print("\n📝 Sample entries (newest first):")
            cursor.execute("SELECT * FROM guestbook ORDER BY timestamp DESC LIMIT 3;")
            for row in cursor.fetchall():
                print(f"\n   🆔 ID: {row[0]}")
                print(f"   👤 Name: {row[1]}")
                print(f"   💬 Message: {row[2]}")
                print(f"   ⏰ When: {row[3]}")
                print(f"   😊 Sentiment: {row[4]}")
        
        conn.close()
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
    
    print("\n✅ Check complete!")

if __name__ == "__main__":
    check_database()
