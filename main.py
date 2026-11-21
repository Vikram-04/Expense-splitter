"""Command-line entry point for the expense splitter."""

from expense import add_expense


def main():
    """Read expenses, calculate settlements, and display the result."""
    from settlement import calculate_settlements

    balances = {}
    expense_count = int(input("Enter number of expenses: "))

    for expense_number in range(1, expense_count + 1):
        print(f"\nExpense {expense_number}")
        payer = input("Who paid? ").strip()
        amount = float(input("Amount: "))
        participants = [
            participant.strip()
            for participant in input(
                "Participants (comma-separated): "
            ).split(",")
            if participant.strip()
        ]
        add_expense(balances, payer, amount, participants)

    settlements = calculate_settlements(balances)

    if not settlements:
        print("Everyone is settled.")
        return

    for debtor, creditor, amount in settlements:
        print(f"{debtor} pays {creditor}: ₹{amount:g}")


if __name__ == "__main__":
    main()
