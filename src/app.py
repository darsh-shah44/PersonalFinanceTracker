from flask import Flask, jsonify

from database import get_db_connection, init_db

app = Flask (__name__)

init_db()

@app.route('/')
def index():
    return "Welcome to the Finance Tracker App!"
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    conn = get_db_connection()
    
    expenses = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()

    conn.close()

    expenses_list = []
    for expense in expenses:
        expenses_list.append({
            'id': expense['id'],
            'amount': expense['amount'],
            'category': expense['category'],
            'description': expense['description'],
            'date': expense['date'],
            'created_at': expense['created_at']
        })

    return jsonify(expenses_list)

if __name__ == '__main__':
    print("Starting server...")
    app.run(debug=True)