Transaction Logger
A Python CLI tool to log and summarize financial transactions using SQLite.

Setup
Ensure Python 3.7+ is installed.

Run python transaction_logger.py to log sample transactions and view summaries.

Sample output:

Added transaction: Salary, $1500.00, 2025-07-22
Added transaction: Groceries, $75.00, 2025-07-22
Added transaction: Utilities, $100.00, 2025-07-22
Added transaction: Rent, $800.00, 2025-07-22

Transaction Summary:
Groceries: $75.00
Rent: $800.00
Salary: $1500.00
Utilities: $100.00
Features
Logs transactions with category, amount, and date.
Generates category-based summary reports.
Black-box testing ensures output accuracy (see test_plan.txt).
Technologies
Python
SQLite
