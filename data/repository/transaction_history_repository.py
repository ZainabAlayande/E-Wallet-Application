from data.model.transaction_history import Transaction


class Transaction_History:
    def save(self, wallet: Transaction) -> Transaction:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def delete_transaction_by_id(self, identity_number: int):
        raise NotImplementedError

    def find_transaction_by_id(self, identity_number: int):
        raise NotImplementedError

    def view_all_transactions(self) -> list[Transaction]:
        raise NotImplementedError
