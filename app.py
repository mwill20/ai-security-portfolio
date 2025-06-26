import os
import sqlite3
from datetime import datetime

import click
from flask import Flask, render_template, request, redirect, url_for
from flask.cli import with_appcontext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def train_sentiment_model():
    """Initializes and trains a simple sentiment analysis model."""
    training_data = [
        ("I love this website!", "positive"),
        ("Great work!", "positive"),
        ("This is amazing!", "positive"),
        ("I don't like this.", "negative"),
        ("This could be better.", "negative"),
        ("Not what I expected.", "negative"),
    ]
    texts = [text for text, _ in training_data]
    labels = [label for _, label in training_data]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    return vectorizer, model

# Initialize model and vectorizer globally
vectorizer, sentiment_model = train_sentiment_model()

def analyze_sentiment(text):
    """Analyzes the sentiment of a given text."""
    X = vectorizer.transform([text])
    return sentiment_model.predict(X)[0]

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.urandom(24),
        DATABASE=os.path.join(app.instance_path, 'portfolio.db'),
    )

    if test_config is not None:
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def get_db_connection():
        conn = sqlite3.connect(app.config['DATABASE'])
        conn.row_factory = sqlite3.Row
        return conn

    def init_db():
        db = get_db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read().decode('utf8'))
        db.commit()
        db.close()

    @click.command('init-db')
    @with_appcontext
    def init_db_command():
        """Clear existing data and create new tables."""
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
        return render_template('projects.html')

    @app.route('/guestbook', methods=['GET', 'POST'])
    def guestbook():
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

