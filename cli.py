import argparse
from database import init_db, add_transaction, get_transactions, delete_transaction, set_budget, get_budget
from reports import generate_monthly_report
from datetime import datetime

def main():
    init_db()  # Ensure database and tables are initialized

    parser = argparse.ArgumentParser(description='Personal Finance Manager')
    subparsers = parser.add_subparsers(dest='command')

    # Add transaction
    parser_add = subparsers.add_parser('add', help='Add a transaction')
    parser_add.add_argument('type', choices=['Income', 'Expense'], help='Type of transaction')
    parser_add.add_argument('category', help='Category of transaction')
    parser_add.add_argument('amount', type=float, help='Amount')
    parser_add.add_argument('-d', '--description', default='', help='Description for the transaction')

    # View transactions
    parser_view = subparsers.add_parser('view', help='View all transactions')

    # Delete transaction
    parser_delete = subparsers.add_parser('delete', help='Delete a transaction')
    parser_delete.add_argument('id', type=int, help='Transaction ID to delete')

    # Set budget
    parser_budget = subparsers.add_parser('budget', help='Set a budget for a given month and category')
    parser_budget.add_argument('month', help='Month in YYYY-MM format')
    parser_budget.add_argument('category', help='Category for the budget')
    parser_budget.add_argument('amount', type=float, help='Budget amount')

    # Check budget (optional)
    parser_getbudget = subparsers.add_parser('getbudget', help='Get budget for a given month and category')
    parser_getbudget.add_argument('month', help='Month in YYYY-MM format')
    parser_getbudget.add_argument('category', help='Category to check budget')

    # Generate monthly report
    parser_report = subparsers.add_parser('report', help='Generate monthly financial report')
    parser_report.add_argument('month', help='Month in YYYY-MM format')

    args = parser.parse_args()

    if args.command == 'add':
        date = datetime.now().strftime('%Y-%m-%d')
        add_transaction(date, args.type, args.category, args.amount, args.description)
        print("Transaction added successfully.")

    elif args.command == 'view':
        transactions = get_transactions()
        if transactions:
            print("\nAll Transactions:")
            print("----------------------------")
            for trans in transactions:
                print(f"ID: {trans[0]}, Date: {trans[1]}, Type: {trans[2]}, Category: {trans[3]}, Amount: ${trans[4]:.2f}, Description: {trans[5]}")
        else:
            print("No transactions found.")

    elif args.command == 'delete':
        delete_transaction(args.id)
        print(f"Transaction with ID {args.id} has been deleted.")

    elif args.command == 'budget':
        set_budget(args.month, args.category, args.amount)
        print(f"Budget of ${args.amount:.2f} set for {args.category} in {args.month}.")

    elif args.command == 'getbudget':
        budget = get_budget(args.month, args.category)
        if budget is not None:
            print(f"Budget for {args.category} in {args.month}: ${budget:.2f}")
        else:
            print(f"No budget set for {args.category} in {args.month}.")

    elif args.command == 'report':
        generate_monthly_report(args.month)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()
