"""Expense recording helpers."""


def add_expense(balances, payer, amount, participants):
    """Apply one equally shared expense to a balances dictionary.

    The payer is credited with the full amount, and every participant is
    charged an equal share.
    """
    if not participants:
        raise ValueError("An expense must have at least one participant.")

    share = amount / len(participants)
    balances[payer] = balances.get(payer, 0) + amount

    for participant in participants:
        balances[participant] = balances.get(participant, 0) - share
