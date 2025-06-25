import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DATABASE'] = os.path.join(app.instance_path, 'portfolio.db')

def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    os.makedirs(app.instance_path, exist_ok=True)
    with app.app_context():
        db = get_db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        db.close()

# Initialize sentiment analysis model
def train_sentiment_model():
    # This is a simple example - in production, use a pre-trained model
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

# Initialize model and vectorizer
vectorizer, sentiment_model = train_sentiment_model()

def analyze_sentiment(text):
    X = vectorizer.transform([text])
    return sentiment_model.predict(X)[0]

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
    # Will be populated with database data in future phases
    return render_template('projects.html')

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        sentiment = analyze_sentiment(message)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        conn = get_db_connection()
        conn.execute('INSERT INTO guestbook (name, message, timestamp, sentiment) VALUES (?, ?, ?, ?)',
                    (name, message, timestamp, sentiment))
        conn.commit()
        conn.close()
        return redirect(url_for('guestbook'))
    
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM guestbook ORDER BY timestamp DESC').fetchall()
    conn.close()
    return render_template('guestbook.html', entries=entries)

if __name__ == '__main__':
    # Create database and tables if they don't exist
    init_db()
    app.run(debug=True)
