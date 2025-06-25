from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Home page
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM uploads')
    items = c.fetchall()
    conn.close()
    return render_template('index.html', items=items)

# Upload handler
@app.route('/upload', methods=['POST'])
def upload():
    title = request.form['title']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO uploads (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
