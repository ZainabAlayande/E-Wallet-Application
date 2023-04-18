from data.model.account import Account
from data.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
    accounts = []
    counter = 0

    def delete(self, identity_number: int) -> None:
        for each_object in self.accounts:
            if identity_number in self.accounts:
                self.accounts.remove(each_object)

    def add(self, account: Account) -> Account:
        self.accounts.append(account)
        self.counter += 1
        return account

    def generate_id(self):
        return len(self.accounts) + 1

    def count(self) -> int:
        return self.counter
