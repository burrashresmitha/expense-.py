class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category].append(amount)
        else:
            self.expenses[category] = [amount]

    def total_expenses(self):
        total = 0
        for category, amounts in self.expenses.items():
            total += sum(amounts)
        return total

    def average_expenses(self, category):
        if category in self.expenses:
            amounts = self.expenses[category]
            return sum(amounts) / len(amounts)
        else:
            return 0

    def analyze_data(self):
        print("Expense Analysis:")
        print("Total Expenses: $", self.total_expenses())
        print("Average Expenses per Category:")
        for category in self.expenses.keys():
            avg_expense = self.average_expenses(category)
            print(f"{category}: ${avg_expense:.2f}")

# Example usage:
tracker = ExpenseTracker()

tracker.add_expense("Groceries", 150.50)
tracker.add_expense("Dining", 80.25)
tracker.add_expense("Groceries", 50.75)
tracker.add_expense("Entertainment", 120.00)
tracker.add_expense("Dining", 65.30)

tracker.analyze_data()
