from flask import Flask, jsonify, request
from datetime import date, datetime
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

@app.route('/api/expenses', methods=['POST'])
def add_expense():
        data = request.get_json()
    
        amount = data.get('amount')
        category = data.get('category')
        description = data.get('description', '')
        date = data.get('date')


        if not amount or not category or not date:
            return jsonify({'error': 'Missing required fields'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
             INSERT INTO expenses (amount, category, description, date, created_at)
            VALUES (?, ?, ?, ?, datetime('now'))
        ''', (amount, category, description, date))

        conn.commit()
        expense_id = cursor.lastrowid
        conn.close()

        return jsonify({
             'id': expense_id,
             'message': 'Expense added successfully'
             }), 201

@app.route('/api/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
     conn = get_db_connection()
     cursor = conn.cursor()

     expense = cursor.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,)).fetchone()

     if expense is None:
          conn.close()
          return jsonify({'error': 'Expense not found'}), 404
     
     cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
     conn.commit()
     conn.close()

     return jsonify({'message': 'Expense deleted successfully'}), 200

@app.route('/api/expenses/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
     data = request.get_json()

     amount = data.get('amount')
     category = data.get('category')
     description = data.get('description', '')
     date = data.get('date')

     if not amount or not category or not date:
          return jsonify({'Error': 'Missing required fields'}), 400
     
     conn = get_db_connection()
     cursor = conn.cursor()

     expense = cursor.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,)).fetchone()

     if expense is None:
          conn.close()
          return jsonify({'error': 'Expense not found'}), 404
     
     cursor.execute('''
        UPDATE expenses
        SET amount = ?, category = ?, description = ?, date = ?
        WHERE id = ?
        ''', (amount, category, description, date, expense_id))

     conn.commit()
     conn.close()

     return jsonify({'message': 'Expense updated successfully'}), 200

if __name__ == '__main__':
    print("Starting server...")
    app.run(debug=True)