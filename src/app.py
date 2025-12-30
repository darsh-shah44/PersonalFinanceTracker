from flask import Flask, jsonify

from database import getDBConnection

app = Flask (__name__)

@app.route('/')
def index():
    return "Welcome to the Finance Tracker App!"
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    conn = get_db_connection()
    
    expenses = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()

    conn.close()

    expensesList = []
    for expense in expenses:
        expensesList.append({
            'id': expense['id'],
            'amount': expense['amount'],
            'category': expense['category'],
            'description': expense['description'],
            'date': expense['date'],
            'created_at': expense['created_at']
        })

    return jsonify(expensesList)

if __name__ == '__main__':
    print("Starting server...")
    app.run(debug=True)