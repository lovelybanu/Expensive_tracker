import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Entertainment, etc.): ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    expense = {"date": date, "category": category, "description": description, "amount": amount}
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Expense List ---")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. Date: {exp['date']}, Category: {exp['category']}, Description: {exp['description']}, Amount: {exp['amount']}")

def category_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for exp in expenses:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]

    print("\n--- Category-wise Expense Summary ---")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Category-wise Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
