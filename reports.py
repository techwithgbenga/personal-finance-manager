import matplotlib.pyplot as plt
from collections import defaultdict
from database import get_transactions
from datetime import datetime

def generate_monthly_report(month):
    transactions = get_transactions()
    income = 0
    expenses = 0
    category_expenses = defaultdict(float)

    for trans in transactions:
        # trans indices: 0: id, 1: date, 2: type, 3: category, 4: amount, 5: description
        trans_date = datetime.strptime(trans[1], '%Y-%m-%d')
        trans_month = trans_date.strftime('%Y-%m')
        if trans_month == month:
            if trans[2] == 'Income':
                income += trans[4]
            elif trans[2] == 'Expense':
                expenses += trans[4]
                category_expenses[trans[3]] += trans[4]

    print(f"\nMonthly Report for {month}:")
    print(f"----------------------------")
    print(f"Total Income  : ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Net Savings   : ${income - expenses:.2f}\n")

    # Pie chart for expenses by category
    if category_expenses:
        categories = list(category_expenses.keys())
        amounts = list(category_expenses.values())
        plt.figure(figsize=(8, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title(f'Expenses by Category for {month}')
        plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
        plt.show()
    else:
        print("No expense data available for this month to generate a chart.")
