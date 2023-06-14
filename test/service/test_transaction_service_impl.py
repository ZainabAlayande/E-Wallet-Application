from unittest import TestCase

from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from services.account_serviceImpl import AccountServiceImpl
from services.transaction_service_impl import TransactionServiceImpl


class TestTransactionServiceImpl(TestCase):
    transaction_service = TransactionServiceImpl()
    account_service = AccountServiceImpl()

    register_request = CreateAccountRequest()
    register_request.set_first_name("Zainab")
    register_request.set_last_name("Winfrey")
    register_request.set_gmail("winfrey@gmail.com")
    register_request.set_password("pass")
    register_request.set_phone_number("08030669508")

    register_request_two = CreateAccountRequest()
    register_request_two.set_first_name("Adams")
    register_request_two.set_last_name("Smith")
    register_request_two.set_gmail("smith@gmail.com")
    register_request_two.set_password("pass")
    register_request_two.set_phone_number("07020202020")

    register_request_three = CreateAccountRequest()
    register_request_three.set_first_name("Ryan")
    register_request_three.set_last_name("Cyprus")
    register_request_three.set_gmail("cyprus@email.com")
    register_request_three.set_password("pass")
    register_request_three.set_phone_number("08023677114")

    login_request = LoginRequest()
    login_request.set_account_number("8030669508")
    login_request.set_password("pass")

    def setUp(self):
        self.account_service.register_account(self.register_request)
        self.account_service.register_account(self.register_request_two)
        self.account_service.register_account(self.register_request_three)
        self.account_service.login(self.login_request)

        deposit_request = DepositRequest()
        deposit_request.set_amount(30000)
        deposit_request.set_receivers_account_number("8030669508")
        deposit_request.set_purpose("No purpose")
        self.account_service.deposit_into(deposit_request)

        transfer_request_two = TransferRequest()
        transfer_request_two.set_amount(5000)
        transfer_request_two.set_sender_account_number("8030669508")
        transfer_request_two.set_receiver_account_number("8023677114")
        self.account_service.transfer(transfer_request_two)

        transfer_request = TransferRequest()
        transfer_request.set_amount(10000)
        transfer_request.set_sender_account_number("8030669508")
        transfer_request.set_receiver_account_number("7020202020")
        self.account_service.transfer(transfer_request)

    def test_find_transaction_by_id(self):
        transaction_response = self.transaction_service.find_transaction_by_account_id(1)
        print("Transaction res -> ", transaction_response)
        expected = """
                    Transaction Type: CREDIT
                    Amount: 3000
                    Account Name: Zainab Winfrey
                    Date and Time: 06/14/2023 10:28PM
                    
                    Transaction Type: DEBIT
                    Amount: 5000
                    Account Name: Ryan Cyprus
                    Date and Time: 06/14/2023 10:50PM
                    
                    Transaction Type: DEBIT
                    Amount: 10000
                    Account Name: Adam Smith
                    Date and Time: 06/14/2023 10:57PM
                    """
        self.assertEqual(expected, transaction_response.__str__())
