import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x350")
        self.root.configure(background='#C9E4CA')  # Set background color to light green

        # Create labels and entry fields for date, category, and amount
        self.date_label = tk.Label(root, text="Date", bg='#C9E4CA')
        self.date_label.pack()
        self.date_entry = tk.Entry(root, width=20)
        self.date_entry.pack()

        self.category_label = tk.Label(root, text="Category", bg='#C9E4CA')
        self.category_label.pack()
        self.category_entry = tk.Entry(root, width=20)
        self.category_entry.pack()

        self.amount_label = tk.Label(root, text="Amount", bg='#C9E4CA')
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root, width=20)
        self.amount_entry.pack()

        # Create a button to add an expense
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense, bg='#87CEEB', fg='white')
        self.add_button.pack()

        # Create a text box to display the expenses
        self.expenses_text = tk.Text(root, width=40, height=10, bg='#C9E4CA', fg='black')
        self.expenses_text.pack()

        # Create a label to display the total expense
        self.total_label = tk.Label(root, text="Total Expense: ₹0.00", bg='#C9E4CA')
        self.total_label.pack()

        # Create a button to clear the expenses
        self.clear_button = tk.Button(root, text="Clear Expenses", command=self.clear_expenses, bg='#87CEEB', fg='white')
        self.clear_button.pack()

        # Initialize the expenses list and total expense
        self.expenses = []
        self.total_expense = 0.0

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()

        if date and category and amount:
            try:
                amount = float(amount)
                expense = {"date": date, "category": category, "amount": amount}
                self.expenses.append(expense)
                self.expenses_text.insert("end", f"{date}: {category} - ₹{amount:.2f}\n\n")
                self.date_entry.delete(0, "end")
                self.category_entry.delete(0, "end")
                self.amount_entry.delete(0, "end")
                self.total_expense += amount
                self.total_label.config(text=f"Total Expense: ₹{self.total_expense:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def clear_expenses(self):
        self.expenses_text.delete("1.0", "end")
        self.expenses = []
        self.total_expense = 0.0
        self.total_label.config(text="Total Expense: ₹0.00")

root = tk.Tk()
expense_tracker = ExpenseTracker(root)
root.mainloop()
