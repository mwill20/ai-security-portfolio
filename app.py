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
    # Step 1: Define the training data with examples of positive, negative, and neutral text.
    # This data is used to teach the model how to classify sentiment.
    training_data = [
        # Positive examples
        ("This is fantastic, thank you!", "positive"),
        ("I'm so happy with this result.", "positive"),
        ("Excellent work, keep it up.", "positive"),
        
        # Negative examples
        ("I'm very disappointed with this.", "negative"),
        ("This is not what I wanted at all.", "negative"),
        ("I regret using this service.", "negative"),
        
        # Neutral examples
        ("The service is adequate.", "neutral"),
        ("It's an average experience.", "neutral"),
        ("I have no strong feelings either way.", "neutral"),
    ]

    # Step 2: Separate the training data into texts and their corresponding labels.
    texts = [text for text, _ in training_data]
    labels = [label for _, label in training_data]

    # Step 3: Convert the text data into numerical vectors using TF-IDF.
    # TF-IDF (Term Frequency-Inverse Document Frequency) reflects how important a word is to a document in a collection.
    # This allows the machine learning model to work with the text data.
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # Step 4: Train a Logistic Regression model.
    # This model learns to predict the sentiment (label) based on the vectorized text (X).
    model = LogisticRegression()
    model.fit(X, labels)

    # Step 5: Return the trained vectorizer and model so they can be used for predictions.
    return vectorizer, model

# Initialize the sentiment analysis model and vectorizer globally when the application starts.
# This ensures the model is trained only once, saving resources on each prediction.
vectorizer, sentiment_model = train_sentiment_model()

def analyze_sentiment(text):
    """Analyzes the sentiment of a given text using the trained model."""
    # Step 1: Transform the input text into a numerical vector using the same vectorizer that was trained on.
    # It's crucial to use the same vectorizer to ensure the input is in the correct format for the model.
    X = vectorizer.transform([text])

    # Step 2: Use the trained model to predict the sentiment of the transformed text.
    # The `predict` method returns an array of predictions; we take the first element since we're only analyzing one text.
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
    else:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError as e:
        print(f"Error creating instance directory: {e}")

    def get_db_connection():
        conn = sqlite3.connect(app.config['DATABASE'])
        conn.row_factory = sqlite3.Row
        return conn

    def init_db():
        try:
            db = get_db_connection()
            with app.open_resource('schema.sql', mode='r') as f:
                sql_script = f.read().decode('utf-8')
                db.executescript(sql_script)
            db.commit()
            click.echo('Database initialized successfully.')
        except Exception as e:
            click.echo(f'Error initializing database: {e}')
        finally:
            if 'db' in locals():
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

    # SQL Injection Demo Page
    @app.route('/sqli-demo')
    def sqli_demo():
        return render_template('sqli_demo.html')
    
    # VULNERABLE endpoint for SQL injection demo
    @app.route('/search/vulnerable')
    def vulnerable_search():
        query = request.args.get('q', '')
        results = []
        
        if query:
            try:
                conn = get_db_connection()
                # WARNING: This is intentionally vulnerable to SQL injection!
                # DO NOT use this pattern in production code!
                cursor = conn.execute(f"SELECT * FROM guestbook WHERE message LIKE '%{query}%'")
                results = cursor.fetchall()
                conn.close()
            except Exception as e:
                results = [f"Error: {str(e)}"]
        
        return render_template('search_results.html', 
                            query=query, 
                            results=results,
                            endpoint='vulnerable',
                            is_vulnerable=True)
    
    # SECURE endpoint for SQL injection demo
    @app.route('/search/secure')
    def secure_search():
        query = request.args.get('q', '')
        results = []
        
        if query:
            try:
                conn = get_db_connection()
                # This is the secure way to handle user input in SQL queries
                cursor = conn.execute(
                    "SELECT * FROM guestbook WHERE message LIKE ?", 
                    (f'%{query}%',)
                )
                results = cursor.fetchall()
                conn.close()
            except Exception as e:
                results = [f"Error: {str(e)}"]
        
        return render_template('search_results.html', 
                            query=query, 
                            results=results,
                            endpoint='secure',
                            is_vulnerable=False)
    
    return app

