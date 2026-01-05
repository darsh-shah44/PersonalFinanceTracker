async function loadExpenses() {
    const response = await fetch('/api/expenses');
    const expenses = await response.json();
    console.log('Expenses:', expenses);

    const tbody = document.getElementById('expenses-list');
    tbody.innerHTML = '';

    expenses.forEach(function(expense){
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${expense.amount}</td>
            <td>${expense.date}</td>
            <td>${expense.category}</td>
            <td>${expense.description}</td>
            <td><button>Delete</button></td>
        `;
        tbody.appendChild(row);
    })
}

async function addExpense(event){
    event.preventDefault();
    
    const amount = document.getElementById('amount').value;
    const category = document.getElementById('category').value;
    const description = document.getElementById('description').value;
    const date = document.getElementById('date').value;

    const response = await fetch('/api/expenses', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'},
        body: JSON.stringify({
            amount: parseFloat(amount),
            category: category,
            description: description,
            date: date
        })
    });

    if(response.ok){
        console.log('Expense added successfully');
        document.getElementById('expense-form').reset();
        loadExpenses();
    }
    else{
        console.error('Failed to add expense');
        alert('Error adding expense');
    }
}

document.addEventListener('DOMContentLoaded', function(){
    loadExpenses();
    document.getElementById('expense-form').addEventListener('submit', addExpense);
});