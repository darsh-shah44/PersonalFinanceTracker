# 💰 Personal Finance Tracker

A full-stack web application for tracking personal expenses with a clean, modern interface.

## 🎯 Features

- **Add Expenses**: Simple form to input amount, category, description, and date
- **View All Expenses**: Dynamic table displaying all tracked expenses
- **Delete Expenses**: Remove expenses with confirmation prompt
- **Real-time Updates**: No page reloads needed - everything updates instantly
- **Categorized Spending**: Organize expenses by Food, Housing, Transportation, Utilities, Entertainment, Shopping, Healthcare, and more
- **Responsive Design**: Clean, modern UI that works on desktop and mobile

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Flask (Web Framework)
- SQLite (Database)

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript (Async/Await, Fetch API)

**Tools:**
- Git & GitHub
- RESTful API design

## 📂 Project Structure
```
PersonalFinanceTracker/
├── src/
│   ├── app.py              # Flask application & API endpoints
│   └── database.py         # Database initialization & connection
├── templates/
│   └── index.html          # Frontend HTML
├── static/
│   ├── app.js              # Frontend JavaScript logic
│   └── style.css           # Styling
├── requirements.txt        # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/YOUR_USERNAME/PersonalFinanceTracker.git
   cd PersonalFinanceTracker
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Run the application**
```bash
   python src/app.py
```

4. **Open in browser**
```
   http://127.0.0.1:5000
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/expenses` | Retrieve all expenses |
| POST | `/api/expenses` | Create new expense |
| PUT | `/api/expenses/<id>` | Update expense by ID |
| DELETE | `/api/expenses/<id>` | Delete expense by ID |

### Example API Usage

**Create Expense:**
```bash
curl -X POST http://127.0.0.1:5000/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount": 50.00, "category": "Food", "description": "Groceries", "date": "2025-01-15"}'
```

**Get All Expenses:**
```bash
curl http://127.0.0.1:5000/api/expenses
```

## 🎓 Learning Outcomes

This project was built to practice:
- Full-stack web development
- RESTful API design
- Asynchronous JavaScript
- Database management
- Git version control
- Frontend-backend integration

## 🔮 Future Enhancements

- [ ] Budget goals and alerts
- [ ] Data visualization (charts/graphs)
- [ ] Export to CSV
- [ ] Monthly/yearly summaries
- [ ] User authentication
- [ ] Multiple currencies support
- [ ] Receipt upload

## 📝 License

This project is open source and available under the MIT License.

## 👤 Darsh Shah

**Your Name**
- GitHub: [@darsh-shah44](https://github.com/darsh-shah44)