import decimal

from InstantPay.data.repository.account_repository_impl import AccountRepositoryImpl
from InstantPay.dtos.request.request_class import CreateAccountRequest
from InstantPay.dtos.response.register_response import RegisterResponse
from InstantPay.services.account_service import AccountService
from InstantPay.utils.mapper import Mapper


class AccountServiceImpl(AccountService):

    def register_account(self, request: CreateAccountRequest) -> RegisterResponse:
        account = Mapper.map_request_with_account(request)
        account_repository = AccountRepositoryImpl()
        response = RegisterResponse()
        account_repository.add(account)
        Mapper.map_account_with_response(account, response)
        return response

    def login(self, account_number: str, password: str) -> bool:
        account_repository = AccountRepositoryImpl()
        account = account_repository.find_by_account_number(account_number)
        if account is None:
            raise ValueError("account not found")
        if account.get_password() != password:
            raise ValueError("invalid credentials")
        return True

    def deposit(self, account_number: str, amount: float) -> bool:
        account_repository = AccountRepositoryImpl()
        account = account_repository.find_by_account_number(account_number)
        if account is None:
            return False
        else:
            account.deposit(amount)
            return True

    def check_balance(self, account_number: str) -> decimal:
        account_repository = AccountRepositoryImpl()
        account = account_repository.find_by_account_number(account_number)
        if account is None:
            return None
        else:
            return account.get_balance()

    def withdraw(self, account_number: str, amount: decimal):
        account_repository = AccountRepositoryImpl()
        account = account_repository.find_by_account_number(account_number)
        if account is None:
            raise ValueError("Account not found")
        else:
            account.withdraw(amount)

    def transfer(self, sender_account_number: str, receiver_account_number: str, amount: decimal):
        account_repository = AccountRepositoryImpl()
        sender_account = account_repository.find_by_account_number(sender_account_number)
        receiver_account = account_repository.find_by_account_number(receiver_account_number)
        if sender_account is None:
            raise ValueError("Sender account not found")
        elif receiver_account is None:
            raise ValueError("Receiver account not found")
        else:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
