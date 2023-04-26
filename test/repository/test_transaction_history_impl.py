from unittest import TestCase

from data.model.transaction_history import Transaction
from data.repository.transaction_history_impl import Transaction_History_Impl


class TestTransaction_History_Impl(TestCase):

    def test_save_one_transaction_count_is_one(self):
        transaction = Transaction()
        transaction_two = Transaction()
        transaction_history = Transaction_History_Impl()
        transaction_history.save(transaction)
        self.assertEqual(1, transaction_history.count())

    def test_save_two_transaction_count_is_two(self):
        transaction = Transaction()
        transaction_two = Transaction()
        transaction_history = Transaction_History_Impl()
        transaction_history.save(transaction)
        transaction_history.save(transaction_two)
        self.assertEqual(2, transaction_history.count())

    def test_delete_transaction_by_id(self):
        transaction = Transaction()
        transaction_two = Transaction()
        transaction_history = Transaction_History_Impl()
        transaction_history.save(transaction)
        self.assertEqual(1, transaction.get_id())
        transaction_history.save(transaction_two)
        self.assertEqual(2, transaction_two.get_id())
        transaction_history.delete_transaction_by_id(1)
        self.assertEqual(1, transaction_history.count())

    def test_view_all_transactions(self):
        transaction = Transaction()
        transaction_two = Transaction()
        transaction_history = Transaction_History_Impl()
        transaction.set_amount(300.0)
        transaction.set_transfer_type("DEBIT")
        transaction.set_senders_name("Anifa")
        transaction_history.save(transaction)

        transaction_two.set_amount(500.0)
        transaction_two.set_transfer_type("CREDIT")
        transaction_two.set_senders_name("Zainab")
        transaction_history.save(transaction_two)

        self.assertEqual(2, transaction_history.count())
        print("Count of trans -> ", transaction_history.count())

        expected = """
        Id: 1
        Amount: 300.0
        Transaction Type: DEBIT
        Sender's Name: Anifa
        
        Id: 2
        Amount: 500.0
        Transaction Type: CREDIT
        Sender's Name: Zainab"""
        self.assertEqual(expected, self.transaction_history.view_all_transactions().__str__())

    def test_debit_transaction_can_be_viewed(self):
        pass

    def test_credit_transaction_can_be_viewed(self):
        pass
