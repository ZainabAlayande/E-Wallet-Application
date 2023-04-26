from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.withdraw_request import WithdrawRequest
from services.account_serviceImpl import AccountServiceImpl

account_service_impl = AccountServiceImpl()


class AccountController:

    @staticmethod
    def register(register_request: CreateAccountRequest) -> object:
        try:
            return account_service_impl.register_account(register_request)
        except ValueError as exception:
            return str(exception)

    @staticmethod
    def login(login_request: LoginRequest) -> object:
        try:
            return account_service_impl.login(login_request)
        except ValueError as exception:
            return str(exception)

    @staticmethod
    def deposit(deposit_request: DepositRequest) -> object:
        try:
            return account_service_impl.deposit_into(deposit_request)
        except ValueError as exception:
            return str(exception)

    @staticmethod
    def check_balance(account_number: str) -> object:
        try:
            return account_service_impl.check_balance(account_number)
        except ValueError as exception:
            return str(exception)

    @staticmethod
    def withdraw(withdraw_request: WithdrawRequest) -> object:
        try:
            return account_service_impl.withdraw_from(withdraw_request)
        except ValueError as exception:
            return str(exception)
