# AI Security Portfolio - Project Summary

This document provides an overview of the AI Security Portfolio project, including its features, setup instructions, and key components for SQL injection testing.

## 🚀 Key Features

### 1. Sentiment Analysis Guestbook
- Users can leave messages that are analyzed for sentiment (positive/negative/neutral)
- Messages are stored in a SQLite database with timestamps
- Built with Flask and scikit-learn

### 2. SQL Injection Demo
- Interactive demo showing vulnerable and secure SQL queries
- Accessible at `/sqli-demo`
- Includes educational examples of SQL injection attempts

### 3. Database Utilities
- `add_test_data.py`: Populates the database with sample messages
- `db_utils.py`: Manages database backups and restores
- `check_db.py`: Inspects database contents

## 🛠️ Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install scikit-learn  # For sentiment analysis
   ```

2. **Initialize the database**:
   ```bash
   python -c "from app import create_app; app = create_app(); app.app_context().push(); from app import init_db; init_db()"
   ```

3. **Add test data**:
   ```bash
   python add_test_data.py
   ```

4. **Run the application**:
   ```bash
   python -m flask run
   ```

## 🔍 SQL Injection Testing

### Demo Endpoints
- `/sqli-demo`: Interactive demo page
- `/search/vulnerable?q=test`: Vulnerable search endpoint
- `/search/secure?q=test`: Secure search endpoint

### Example Tests
- Show all messages: `' OR '1'='1`
- View database schema: `' UNION SELECT name, sql, 3, 4, 5 FROM sqlite_master WHERE type='table' --`

## 📂 Database Management

### Backups
```bash
# Create a backup
python db_utils.py backup

# List available backups
python db_utils.py list

# Restore from backup
python db_utils.py restore [backup_name]
```

## ⚠️ Security Notes
- The vulnerable endpoints are for educational purposes only
- Never use the vulnerable code patterns in production
- The database is stored in `instance/portfolio.db` (not version controlled)

## 📝 Project Structure
- `app.py`: Main Flask application
- `templates/`: HTML templates
- `static/`: CSS and JavaScript files
- `instance/`: Database file (created at runtime)
- `backups/`: Database backups (created by `db_utils.py`)

## 🤝 Contributing
When adding new features:
1. Always use parameterized queries
2. Add tests for new functionality
3. Update this document with any new features or changes
