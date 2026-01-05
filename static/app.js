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

document.addEventListener('DOMContentLoaded', loadExpenses);