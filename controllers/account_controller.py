from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.withdraw_request import WithdrawRequest
from services.account_serviceImpl import AccountServiceImpl

account_service_impl = AccountServiceImpl()


class AccountController:

    def __init__(self):
        pass

    def register(self, register_request: CreateAccountRequest) -> object:
        try:
            return account_service_impl.register_account(register_request)
        except ValueError:
            return

    def login(self, login_request: LoginRequest) -> object:
        try:
            return account_service_impl.login(login_request)
        except ValueError:
            return

    def deposit(self, deposit_request: DepositRequest) -> object:
        try:
            return account_service_impl.deposit_into(deposit_request)
        except ValueError:
            return

    def check_balance(self, account_number: str) -> object:
        try:
            return account_service_impl.check_balance(account_number)
        except ValueError:
            return

    def withdraw(self, withdraw_request: WithdrawRequest) -> object:
        try:
            return account_service_impl.withdraw(withdraw_request)
        except ValueError:
            return
