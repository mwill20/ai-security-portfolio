import shutil
import os
from datetime import datetime

def backup_db():
    """Create a timestamped backup of the database"""
    db_path = os.path.join('instance', 'portfolio.db')
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False
        
    # Create backups directory if it doesn't exist
    os.makedirs('backups', exist_ok=True)
    
    # Create backup filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join('backups', f'portfolio_backup_{timestamp}.db')
    
    # Copy the database file
    shutil.copy2(db_path, backup_path)
    print(f"✅ Database backed up to: {backup_path}")
    return True

def restore_db(backup_name=None):
    """Restore database from a backup"""
    backups_dir = 'backups'
    if not os.path.exists(backups_dir):
        print("❌ No backups directory found!")
        return False
    
    # List available backups
    backups = [f for f in os.listdir(backups_dir) if f.endswith('.db')]
    
    if not backups:
        print("❌ No backup files found!")
        return False
    
    # If no specific backup specified, use the most recent
    if not backup_name:
        backup_name = sorted(backups)[-1]  # Get most recent backup
    
    backup_path = os.path.join(backups_dir, backup_name)
    if not os.path.exists(backup_path):
        print(f"❌ Backup file not found: {backup_name}")
        print(f"Available backups: {', '.join(backups)}")
        return False
    
    # Restore the backup
    db_path = os.path.join('instance', 'portfolio.db')
    shutil.copy2(backup_path, db_path)
    print(f"✅ Database restored from: {backup_name}")
    return True

def list_backups():
    """List all available database backups"""
    backups_dir = 'backups'
    if not os.path.exists(backups_dir):
        print("No backups directory found")
        return []
    
    backups = sorted([f for f in os.listdir(backups_dir) if f.endswith('.db')])
    if not backups:
        print("No backup files found")
        return []
    
    print("\nAvailable backups:")
    for i, backup in enumerate(backups, 1):
        print(f"{i}. {backup}")
    
    return backups

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python db_utils.py [backup|restore|list]")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'backup':
        backup_db()
    elif command == 'restore':
        if len(sys.argv) > 2:
            restore_db(sys.argv[2])
        else:
            restore_db()
    elif command == 'list':
        list_backups()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: backup, restore, list")
