from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit,
    QTableWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem, QHeaderView, QMessageBox
)
from PyQt6.QtCore import QDateTime
from database import fetch_expenses, add_expense, delete_expense

class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.load_data()  # Load data when the UI is initialized

    def settings(self):
        self.setGeometry(750, 300, 500, 600)
        self.setWindowTitle("Expense Tracker")
        
    def initUI(self):
        # Create all objects
        self.date_box = QDateEdit()
        self.date_box.setCalendarPopup(True)
        self.date_box.setDateTime(QDateTime.currentDateTime())

        self.dropdown = QComboBox()
        self.dropdown.addItem("Select Category")
        self.dropdown.addItem("Food")
        self.dropdown.addItem("Transport")
        self.dropdown.addItem("Utilities")
        self.dropdown.addItem("Entertainment")
        self.dropdown.addItem("Others")

        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Enter amount")

        self.description = QLineEdit()
        self.description.setPlaceholderText("Enter description")

        self.btn_add = QPushButton("Add Expense")
        self.btn_delete = QPushButton("Delete Expense")

        # Connect buttons to their functions
        self.btn_add.clicked.connect(self.add_expense)
        self.btn_delete.clicked.connect(self.delete_expense)

        # Setup table
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Amount", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Add widgets to layout
        self.setup_layout()
        self.apply_styles()

    def setup_layout(self):
        master = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        # Row 1
        row1.addWidget(QLabel("Date"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category"))
        row1.addWidget(self.dropdown)

        # Row 2
        row2.addWidget(QLabel("Amount"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description"))
        row2.addWidget(self.description)
        row2.addWidget(self.btn_add)
        row2.addWidget(self.btn_delete)

        # Add rows to master layout
        master.addLayout(row1)
        master.addLayout(row2)
        master.addWidget(self.table)

        self.setLayout(master)

    def load_data(self):
        # Load data from the database and populate the table
        expenses = fetch_expenses()
        self.table.setRowCount(0)  # Clear existing data
        for expense in expenses:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(str(expense["id"])))
            self.table.setItem(row_position, 1, QTableWidgetItem(expense["date"]))
            self.table.setItem(row_position, 2, QTableWidgetItem(expense["category"]))
            self.table.setItem(row_position, 3, QTableWidgetItem(str(expense["amount"])))
            self.table.setItem(row_position, 4, QTableWidgetItem(expense["description"]))

    def add_expense(self):
        # Get values from input fields
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        # Validate inputs
        if category == "Select Category" or not amount or not description:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Amount must be a number.")
            return

        # Add expense to the database
        if add_expense(date, category, amount, description):
            QMessageBox.information(self, "Success", "Expense added successfully.")
            self.load_data()  # Refresh the table
        else:
            QMessageBox.critical(self, "Error", "Failed to add expense.")

    def delete_expense(self):
        # Get selected row
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Selection Error", "Please select an expense to delete.")
            return

        # Get the expense ID from the table
        expense_id = int(self.table.item(selected_row, 0).text())

        # Delete expense from the database
        if delete_expense(expense_id):
            QMessageBox.information(self, "Success", "Expense deleted successfully.")
            self.load_data()  # Refresh the table
        else:
            QMessageBox.critical(self, "Error", "Failed to delete expense.")

    def apply_styles(self):
        # Apply styles to make the UI look more modern
        self.setStyleSheet("""
            QWidget {
                font-family: 'Arial';
                font-size: 12px;
            }
            QLineEdit, QComboBox, QDateEdit {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QTableWidget {
                border: 1px solid #ddd;
                gridline-color: #eee;
            }
            QHeaderView::section {
                background-color: blue;
                padding: 5px;
                border: 1px solid #ddd;
            }
        """)