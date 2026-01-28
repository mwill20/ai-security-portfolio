import os
import sqlite3
from datetime import datetime

import click
from flask import Flask, render_template, request, redirect, url_for
from flask.cli import with_appcontext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Import projects data
try:
    from projects_data import projects as projects_list
except ImportError:
    projects_list = {}

def train_sentiment_model():
    """Initializes and trains a simple sentiment analysis model."""
    training_data = [
        ("This is fantastic, thank you!", "positive"),
        ("I'm so happy with this result.", "positive"),
        ("Excellent work, keep it up.", "positive"),
        ("I'm very disappointed with this.", "negative"),
        ("This is not what I wanted at all.", "negative"),
        ("I regret using this service.", "negative"),
        ("The service is adequate.", "neutral"),
        ("It's an average experience.", "neutral"),
        ("I have no strong feelings either way.", "neutral"),
    ]
    texts = [text for text, _ in training_data]
    labels = [label for _, label in training_data]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    return vectorizer, model

# Initialize model globally (mock training for demo purposes if sklearn fails in some envs, but here we assume it works)
try:
    vectorizer, sentiment_model = train_sentiment_model()
except Exception as e:
    print(f"Warning: Sentiment model training failed: {e}")
    vectorizer, sentiment_model = None, None

def analyze_sentiment(text):
    if not vectorizer or not sentiment_model:
        return "neutral"
    X = vectorizer.transform([text])
    return sentiment_model.predict(X)[0]

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.urandom(24),
        DATABASE=os.path.join(app.instance_path, 'portfolio.db'),
    )

    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile('config.py', silent=True)

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    def get_db_connection():
        conn = sqlite3.connect(app.config['DATABASE'])
        conn.row_factory = sqlite3.Row
        return conn

    def init_db():
        db = get_db_connection()
        # Create table if not exists (schema.sql content typically)
        db.execute('''
            CREATE TABLE IF NOT EXISTS guestbook (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL,
                sentiment TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()
        db.close()

    @click.command('init-db')
    @with_appcontext
    def init_db_command():
        init_db()
        click.echo('Initialized the database.')

    app.cli.add_command(init_db_command)

    @app.context_processor
    def inject_now():
        return {'now': datetime.now()}

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/projects')
    def projects():
        return render_template('projects.html', projects=projects_list)
        
    @app.route('/sagevault')
    def sagevault():
        return render_template('sagevault.html')

    @app.route('/guestbook', methods=['GET', 'POST'])
    def guestbook():
        # Ensure table exists cheaply
        try:
             with sqlite3.connect(app.config['DATABASE']) as conn:
                conn.execute("SELECT 1 FROM guestbook LIMIT 1")
        except sqlite3.OperationalError:
            init_db()

        conn = get_db_connection()
        if request.method == 'POST':
            name = request.form['name']
            message = request.form['message']
            sentiment = analyze_sentiment(message)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            conn.execute(
                'INSERT INTO guestbook (name, message, timestamp, sentiment) VALUES (?, ?, ?, ?)',
                (name, message, timestamp, sentiment)
            )
            conn.commit()
            conn.close()
            return redirect(url_for('guestbook'))
        
        entries = conn.execute('SELECT * FROM guestbook ORDER BY timestamp DESC').fetchall()
        conn.close()
        return render_template('guestbook.html', entries=entries)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
