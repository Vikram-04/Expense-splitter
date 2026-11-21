# Collaborative Expense Splitter

## Project Overview

A simple Python CLI application that splits expenses among a group of people and calculates the minimum number of transactions required to settle everyone's debts.

The project is divided into two independent modules so two developers can work simultaneously.

## Project Structure

```text
expense-splitter/
│
├── main.py
├── expense_manager.py
├── settlement.py
├── README.md
└── tests/
    ├── test_expense_manager.py
    └── test_settlement.py
```

## Module Responsibilities

### 1. Expense Manager — Developer 1

File: `expense_manager.py`

Responsible for recording expenses and calculating each person's net balance.

**Required functions:**

```python
def add_expense(balances, payer, amount, participants):
    pass
```

- `balances`: Dictionary storing each person's net balance.
- `payer`: Person who paid the expense.
- `amount`: Total expense amount.
- `participants`: List of people sharing the expense.

**Logic:**

- The payer gets credited with the full amount.
- Each participant gets debited with their equal share.
- Update the balances dictionary.

Example:

```python
balances = {}

add_expense(balances, "Alice", 600, ["Alice", "Bob", "Charlie"])

# Expected:
# {
#     "Alice": 400,
#     "Bob": -200,
#     "Charlie": -200
# }
```

### 2. Settlement Calculator — Developer 2

File: `settlement.py`

Responsible for calculating who should pay whom to settle all outstanding balances with the minimum number of transactions.

**Required function:**

```python
def calculate_settlements(balances):
    pass
```

**Input:**

```python
{
    "Alice": 400,
    "Bob": -200,
    "Charlie": -200
}
```

**Expected output:**

```python
[
    ("Bob", "Alice", 200),
    ("Charlie", "Alice", 200)
]
```

Each tuple represents:

```python
(debtor, creditor, amount)
```

**Requirements:**

- Identify creditors (positive balances).
- Identify debtors (negative balances).
- Match debtors with creditors.
- Minimize the number of transactions.
- Handle zero balances correctly.
- Return an empty list if everyone is settled.

Use a greedy settlement algorithm.

## Integration — main.py

The main application will combine both modules.

Expected workflow:

1. Initialize an empty balances dictionary.
2. Accept expenses from users.
3. Call `add_expense()` for every expense.
4. Pass the final balances to `calculate_settlements()`.
5. Display the settlement transactions.

## Collaboration Guidelines

We will use Git and GitHub to collaborate.

1. Clone the shared repository.
2. Create separate branches:
   - `feature/expense-manager`
   - `feature/settlement-calculator`
3. Work only on your assigned module.
4. Commit changes with meaningful commit messages.
5. Push your branch to GitHub.
6. Create a Pull Request.
7. Review and merge the changes into `main`.

## Important Collaboration Rule

Both developers must follow the function signatures and input/output formats defined above.

Do not modify the other developer's module without discussing it first.

## Definition of Done

- [ ] Both modules work independently.
- [ ] Both modules are integrated into `main.py`.
- [ ] Expense calculations are correct.
- [ ] Settlement calculations are correct.
- [ ] Edge cases are tested.
- [ ] Changes are merged through Pull Requests.
- [ ] The application runs successfully.
