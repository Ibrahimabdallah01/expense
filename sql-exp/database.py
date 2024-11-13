# All SQL-related imports
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def init_db(db_name):
    # Initialize and connect to the database
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName(db_name)
    
    if not database.open():
        return False

    query = QSqlQuery()
    # Corrected SQL query
    query.exec("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    """)
    
    return True

def fetch_expenses():
    # Fetch all expense records from the database
    query = QSqlQuery()
    query.exec("SELECT * FROM expenses")
    
    expenses = []
    while query.next():
        expense = {
            "id": query.value(0),
            "date": query.value(1),
            "category": query.value(2),
            "amount": query.value(3),
            "description": query.value(4)
        }
        expenses.append(expense)
    
    return expenses

def add_expense(date, category, amount, description):
    # Add a new expense record to the database
    query = QSqlQuery()
    query.prepare("""
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    """)
    query.addBindValue(date)
    query.addBindValue(category)
    query.addBindValue(amount)
    query.addBindValue(description)
    
    if not query.exec():
        print("Error adding expense:", query.lastError().text())
        return False
    return True

def delete_expense(expense_id):
    # Delete an expense record by ID
    query = QSqlQuery()
    query.prepare("DELETE FROM expenses WHERE id = ?")
    query.addBindValue(expense_id)
    
    if not query.exec():
        print("Error deleting expense:", query.lastError().text())
        return False
    return True
