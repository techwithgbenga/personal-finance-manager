# Personal Finance Manager

A command-line application to manage your personal finances. This tool allows you to add, view, and delete financial transactions; set monthly budgets; and generate monthly reports with visualizations.

## Features

- **Transaction Management:** Log income and expense transactions.
- **Budgeting:** Set and view monthly budgets by category.
- **Reporting:** Generate monthly financial summaries and pie chart visualizations for expenses.
- **Data Persistence:** Uses SQLite to store all data locally.
- **CLI Interface:** Easy-to-use command-line interface for all operations.

## File Structure
```plaintext
personal_finance_manager/
├── finance_manager.py # Main entry point for the application
├── database.py # Database operations using SQLite
├── reports.py # Generation of financial reports and visualizations
├── cli.py # Command-line interface for user interactions
├── requirements.txt # List of dependencies
└── README.md # Project documentation
```
---

## Setup & Installation

1. **Clone the Repository:**
```bash
   git clone https://github.com/techwithgbenga/personal_finance_manager.git
   cd personal_finance_manager
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Usage:
- To add a transaction:

```bash
python finance_manager.py add Income Salary 5000 "Monthly salary"
python finance_manager.py add Expense Groceries 150 "Weekly groceries"
```
- To view transactions:
```bash
python finance_manager.py view
```
- To delete a transaction by ID:
```bash
python finance_manager.py delete 3
```

- To set a budget:
```bash
python finance_manager.py budget 2025-04 Food 600
```

- To get a set budget:
```bash
python finance_manager.py getbudget 2025-04 Food
```

- To generate a monthly report:
```bash
python finance_manager.py report 2025-04
```

---

## Future Enhancements
- Add a graphical user interface (GUI).
- Integrate more advanced budgeting features.
- Export and import data (e.g., CSV, Excel).
- Pull requests and contributions are welcome. Enjoy managing your personal finances with this tool!

---

## Summary

This **Personal Finance Manager** project is designed to help users track their financial transactions, manage budgets, and understand their monthly spending through a simple CLI and visual reporting. Feel free to extend the project with additional features or a graphical interface.

Would you like to add any other functionalities or make adjustments to this project?
