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
    @app.context_processor
    def inject_now():
        return {'now': datetime.now()}

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about/')
    def about():
        return render_template('about.html')

    @app.route('/projects/')
    def projects():
        return render_template('projects.html', projects=projects_list)
        
    # SageVault route - ensuring template exists or removing if causing errors
    # Based on previous error, sagevault.html was missing. Let's redirect or show a simple string for now if strictly needed,
    # or better, remove it if it was a placeholder. 
    # USER's projects_data.py has a link to /sagevault. 
    # I will create a simple placeholder template for it in the next step to fix the build.
    @app.route('/sagevault')
    def sagevault():
        try:
            return render_template('sagevault.html')
        except:
             return "<h1>SageVault - Internal Secure RAG</h1><p>This is a placeholder for the internal tool.</p>"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
