from InstantPay.data.model.account import Account


class AccountRepository:
    def add(self, account: Account) -> Account:
        pass

    def count(self) -> int:
        raise ImportError

    def delete(self, delete_by_id: int) -> None:
        raise NotImplementedError

    def find_by_account_number(self, account_number) -> Account:
        pass
