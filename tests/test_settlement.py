"""
Unit tests for the Settlement Calculator module (settlement.py).
"""

import unittest
from settlement import calculate_settlements


class TestSettlement(unittest.TestCase):
    def test_readme_example(self):
        """Test the exact example provided in the README."""
        balances = {
            "Alice": 400,
            "Bob": -200,
            "Charlie": -200,
        }
        expected = [
            ("Bob", "Alice", 200),
            ("Charlie", "Alice", 200),
        ]
        result = calculate_settlements(balances)
        self.assertEqual(result, expected)

    def test_empty_balances(self):
        """Test with empty dictionary."""
        self.assertEqual(calculate_settlements({}), [])

    def test_all_zeros(self):
        """Test when everyone is already settled with zero balance."""
        balances = {
            "Alice": 0,
            "Bob": 0,
            "Charlie": 0,
        }
        self.assertEqual(calculate_settlements(balances), [])

    def test_zeros_mixed_with_active_balances(self):
        """Test that zero-balance participants are omitted from settlements."""
        balances = {
            "Alice": 200,
            "Bob": -200,
            "Charlie": 0,
            "Dave": 0.0,
        }
        expected = [
            ("Bob", "Alice", 200),
        ]
        self.assertEqual(calculate_settlements(balances), expected)

    def test_single_debtor_single_creditor(self):
        """Test a simple direct transfer between two people."""
        balances = {
            "Alice": 150,
            "Bob": -150,
        }
        expected = [
            ("Bob", "Alice", 150),
        ]
        self.assertEqual(calculate_settlements(balances), expected)

    def test_multiple_creditors_and_debtors(self):
        """
        Test multiple debtors and creditors.
        A: +300, B: +100
        C: -250, D: -150
        C owes 250 -> pays A 250 (A now needs 50)
        D owes 150 -> pays B 100 (B settled, D owes 50)
        D pays A 50 (both settled)
        """
        balances = {
            "Alice": 300,
            "Bob": 100,
            "Charlie": -250,
            "Dave": -150,
        }
        result = calculate_settlements(balances)

        # Verify that all debts are fully resolved
        net_after = dict(balances)
        for debtor, creditor, amount in result:
            net_after[debtor] += amount
            net_after[creditor] -= amount

        for person, remaining in net_after.items():
            self.assertAlmostEqual(remaining, 0, places=2)

        # Expected minimal transactions: 3 transactions instead of 4
        self.assertEqual(len(result), 3)

    def test_floating_point_balances(self):
        """Test with fractional / floating-point balances."""
        balances = {
            "Alice": 66.67,
            "Bob": -33.33,
            "Charlie": -33.34,
        }
        result = calculate_settlements(balances)
        self.assertTrue(len(result) >= 1)

        # Verify balances balance out
        net_after = dict(balances)
        for debtor, creditor, amount in result:
            net_after[debtor] += amount
            net_after[creditor] -= amount

        for person, remaining in net_after.items():
            self.assertAlmostEqual(remaining, 0, places=1)


if __name__ == "__main__":
    unittest.main()
