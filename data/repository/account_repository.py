from data.model.account import Account


class AccountRepository:
    def add(self, account: Account) -> Account:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def delete(self, delete_by_id: int) -> None:
        raise NotImplementedError


