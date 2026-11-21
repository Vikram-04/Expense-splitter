"""
Settlement Calculator Module

Responsible for calculating who should pay whom to settle all outstanding
balances with the minimum number of transactions using a greedy settlement algorithm.
"""

from typing import Dict, List, Tuple, Union


def calculate_settlements(
    balances: Dict[str, Union[int, float]]
) -> List[Tuple[str, str, Union[int, float]]]:
    """
    Calculate the settlements required to clear all outstanding debts.

    Uses a greedy settlement algorithm:
    1. Filter out participants with a zero (or near-zero) balance.
    2. Separate participants into debtors (negative balance) and creditors (positive balance).
    3. Greedily match the debtor who owes the most with the creditor who is owed the most.
    4. Settle the minimum of the two amounts and update remaining balances.
    5. Repeat until all balances are settled within numerical precision.

    Args:
        balances: A dictionary mapping person names to their net balance.
                  Positive balance = creditor (owed money).
                  Negative balance = debtor (owes money).
                  Zero balance = settled.

    Returns:
        A list of tuples in the format (debtor, creditor, amount).
        Returns an empty list if everyone is already settled or input is empty.
    """
    if not balances:
        return []

    EPSILON = 1e-4

    # Separate into debtors and creditors, ignoring zero/near-zero balances.
    # Debt is recorded as a positive number: debt = -balance
    debtors: List[List[Union[str, float]]] = []
    creditors: List[List[Union[str, float]]] = []

    for person, balance in balances.items():
        rounded_balance = round(float(balance), 2)
        if rounded_balance < -EPSILON:
            debtors.append([person, -rounded_balance])
        elif rounded_balance > EPSILON:
            creditors.append([person, rounded_balance])

    settlements: List[Tuple[str, str, Union[int, float]]] = []

    while debtors and creditors:
        # Sort so largest debt / credit comes first.
        # Secondary sort by person name for consistent, deterministic order.
        debtors.sort(key=lambda x: (-x[1], str(x[0])))
        creditors.sort(key=lambda x: (-x[1], str(x[0])))

        debtor_entry = debtors[0]
        creditor_entry = creditors[0]

        debtor = debtor_entry[0]
        debt = debtor_entry[1]

        creditor = creditor_entry[0]
        credit = creditor_entry[1]

        settle_amount = round(min(debt, credit), 2)

        if settle_amount > EPSILON:
            # Format as integer if no decimal part
            formatted_amount = (
                int(settle_amount) if settle_amount.is_integer() else settle_amount
            )
            settlements.append((debtor, creditor, formatted_amount))

        remaining_debt = round(debt - settle_amount, 2)
        remaining_credit = round(credit - settle_amount, 2)

        if remaining_debt > EPSILON:
            debtor_entry[1] = remaining_debt
        else:
            debtors.pop(0)

        if remaining_credit > EPSILON:
            creditor_entry[1] = remaining_credit
        else:
            creditors.pop(0)

    return settlements
