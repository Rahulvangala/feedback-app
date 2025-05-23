from flask import Flask, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE feedback (
        name TEXT,
        email TEXT,
        gender TEXT,
        interests TEXT,
        comments TEXT
    )
''')

conn.commit()

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    gender = request.form.get('gender')
    interests = request.form.getlist('interests')
    comments = request.form.get('comments')

    if not name or not email or not gender:
        return "Submission Failed: Missing Required Fields"

    cursor.execute('''
        INSERT INTO feedback (name, email, gender, interests, comments)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, email, gender, ', '.join(interests), comments))
    conn.commit()
    
    return f"Feedback Received from {name} ({email}) - Gender: {gender}, Interests: {', '.join(interests)}, Comments: {comments}"

if __name__ == '__main__':
    app.run(port=5001) 
