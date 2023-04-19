from typing import Any

from InstantPay.data.model.account import Account
from InstantPay.data.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
    accounts: list[Account] = []

    def delete(self, account_number: str) -> None:
        for account in self.accounts:
            if account.get_account_number() == account_number:
                self.accounts.remove(account)
                break

    def add(self, account: Account) -> Account:
        account_number = self.generate_account_number(account.get_phone_number())
        account.set_account_number(account_number)
        self.accounts.append(account)
        return account

    @staticmethod
    def generate_account_number(phone_number: str) -> str:
        phone_number = phone_number.lstrip("0")
        account_number = phone_number
        return account_number

    def count(self) -> int:
        return len(self.accounts)

    def find_by_account_number(self, account_number: str) -> Account:
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
