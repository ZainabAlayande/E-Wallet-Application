from data.model.transaction_history import Transaction
from data.repository.transaction_history_repository import Transaction_History


class Transaction_History_Impl(Transaction_History):
    transactions = []
    counter = 0

    def save(self, transaction: Transaction) -> Transaction:
        if transaction.get_id() == 0:
            transaction.set_id(self.generate_transaction_id())
        self.transactions.append(transaction)
        self.counter += 1
        return transaction

    def generate_transaction_id(self) -> int:
        return self.counter + 1

    def count(self) -> int:
        return self.counter

    def find_transaction_by_id(self, identity_number: int):
        for transaction in self.transactions:
            if transaction.get_id() == identity_number:
                return transaction

    def delete_transaction_by_id(self, identity_number: int):
        for transaction in self.transactions:
            if transaction.get_id == identity_number:
                self.transactions.remove(transaction)
            self.counter -= 1
            break

    def view_all_transactions(self) -> list[Transaction]:
        return self.transactions
