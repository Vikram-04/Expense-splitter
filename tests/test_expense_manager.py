import unittest
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from expense import add_expense


class TestAddExpense(unittest.TestCase):
    def test_splits_expense_equally(self):
        balances = {}

        add_expense(balances, "Alice", 600, ["Alice", "Bob", "Charlie"])

        self.assertEqual(
            balances,
            {"Alice": 400, "Bob": -200, "Charlie": -200},
        )

    def test_updates_existing_balances(self):
        balances = {"Alice": 100, "Bob": -100}

        add_expense(balances, "Alice", 300, ["Alice", "Bob"])

        self.assertEqual(balances, {"Alice": 250, "Bob": -250})

    def test_rejects_expense_without_participants(self):
        with self.assertRaises(ValueError):
            add_expense({}, "Alice", 100, [])


if __name__ == "__main__":
    unittest.main()
