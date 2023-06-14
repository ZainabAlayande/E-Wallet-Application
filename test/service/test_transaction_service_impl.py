from unittest import TestCase

from services.transaction_service_impl import TransactionServiceImpl


class TestTransactionServiceImpl(TestCase):
    transaction_service = TransactionServiceImpl()

    def test_find_transaction_by_id(self):
        transaction_response = self.transaction_service.find_transaction_by_id(1)
        expected = """
                    Transaction Type: DEBIT
                    Amount: 1000.0
                    Account Name: Zainab Winfrey
                    Date and Time: 06/14/2023 4:33PM
                    """
        self.assertEqual(expected, transaction_response)
