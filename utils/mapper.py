from InstantPay.data.model.account import Account
from InstantPay.data.repository.account_repository_impl import AccountRepositoryImpl
from InstantPay.dtos.request.request_class import CreateAccountRequest
from InstantPay.dtos.response.register_response import RegisterResponse


class Mapper:

    @staticmethod
    def map_request_with_account(request: CreateAccountRequest) -> Account:
        account = Account()
        account.set_pin(request.get_pin())
        account.set_last_name(request.get_last_name())
        account.set_first_name(request.get_first_name())
        account.set_phone_number(request.get_phone_number())
        account.set_password(request.get_password())
        return account

    @staticmethod
    def map_account_with_response(account: Account, response: RegisterResponse):
        if account is not None:
            response.set_account_number(account.get_account_number())
            response.set_full_name(account.get_first_name() + " " + account.get_last_name())
            response.set_balance(account.get_balance())
