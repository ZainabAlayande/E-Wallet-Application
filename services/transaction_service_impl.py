from data.model.transaction import Transaction
from data.repository.transaction_repository_impl import TransactionRepositoryImpl
from dtos.response.transaction_response import TransactionResponse
from services.transaction_service import TransactionService
from utils.mapper import Mapper


class TransactionServiceImpl(TransactionService):
    transaction_repository = TransactionRepositoryImpl()

    def find_all_transaction(self) -> TransactionResponse:
        pass

    def find_transaction_by_id(self, identity_number: int) -> TransactionResponse:
        found_transaction: Transaction = self.transaction_repository.find_transaction_by_id(identity_number)
        transaction_response: TransactionResponse = Mapper.map_transaction_to_transaction_response(found_transaction)
        return transaction_response

    def view_all_debit_transaction(self):
        pass

    def view_all_credit_transaction(self):
        pass

    def print_bank_statement(self):
        pass