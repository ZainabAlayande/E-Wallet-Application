import decimal

from data.model.transaction import Transaction
from data.model.transaction_type import TransactionType
from data.repository.transaction_repository_impl import TransactionRepositoryImpl
from dtos.request.deposit_request import DepositRequest
from dtos.response.transaction_response import TransactionResponse
from services.transaction_service import TransactionService
from utils.mapper import Mapper


class TransactionServiceImpl(TransactionService):
    transaction_repository = TransactionRepositoryImpl()

    def find_all_transaction(self) -> TransactionResponse:
        pass

    def find_transaction_by_account_id(self, identity_number: int) -> TransactionResponse:
        found_transaction: Transaction = self.transaction_repository.find_transaction_by_id(identity_number)
        transaction_response: TransactionResponse = Mapper.map_transaction_to_transaction_response(found_transaction)
        return transaction_response

    def view_all_debit_transaction(self):
        pass

    def view_all_credit_transaction(self):
        pass

    def print_bank_statement(self):
        pass

    def build_customer_transaction(self, deposit_request: DepositRequest, account_id):
        transaction = Transaction()
        transaction.set_amount(deposit_request.get_amount())
        transaction.set_account_name(deposit_request.get_receivers_account_name())
        transaction.set_transfer_type(deposit_request.get_transaction_type())
        transaction.set_account_id(account_id)
        self.transaction_repository.save(transaction)
