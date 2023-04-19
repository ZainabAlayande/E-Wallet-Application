import decimal

from InstantPay.dtos.request.request_class import CreateAccountRequest
from InstantPay.dtos.response.register_response import RegisterResponse


class AccountService:
    def register_account(self, request: CreateAccountRequest) -> RegisterResponse:
        raise NotImplementedError

    def login(self, account_number: str, password: str) -> bool:
        raise NotImplementedError

    def deposit(self, account_number: str, amount: float) -> bool:
        pass

    def check_balance(self, account_number: str) -> decimal:
        pass

    def withdraw(self, amount: decimal, account_number: str):
        pass

    def transfer(self, sender_account_number: str, receiver_account_number: str, amount: decimal):
        pass