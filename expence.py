class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)

    def view_summary(self):
        print("Expense Summary:")
        total_expense = 0
        for category, amounts in self.expenses.items():
            category_total = sum(amounts)
            total_expense += category_total
            print(f"{category}: ${category_total}")
        print(f"Total Expense: ${total_expense}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            tracker.add_expense(amount, category)
            print("Expense added successfully.")
        elif choice == '2':
            tracker.view_summary()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
