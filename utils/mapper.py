from data.model.account import Account
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.response.deposit_response import DepositResponse
from dtos.response.login_response import LoginResponse
from dtos.response.register_response import RegisterResponse


class Mapper:

    @staticmethod
    def map_request_with_account(request: CreateAccountRequest) -> Account:
        account = Account()
        account.set_gmail(request.get_gmail())
        account.set_last_name(request.get_last_name())
        account.set_first_name(request.get_first_name())
        account.set_phone_number(request.get_phone_number())
        account.set_password(request.get_password())
        return account

    @staticmethod
    def map_account_with_response(account: Account):
        response = RegisterResponse()
        response.set_account_number(account.get_account_number())
        response.set_gmail(account.get_gmail())
        response.set_full_name(account.get_first_name() + " " + account.get_last_name())
        response.set_balance(account.get_balance())
        return response

    # @staticmethod
    # def map_deposit_request_to_response(deposit_request: DepositRequest):
    #     account = Account()
    #     account.set_first_name(deposit_request.get_receivers_account_number())

    @staticmethod
    def map_deposit_request_to_response(deposit_request: DepositRequest):
        response = DepositResponse()
        response.set_senders_name(deposit_request.get_senders_name())
        response.set_receiver_account(deposit_request.get_receivers_account_number())
        response.set_receivers_name(deposit_request.get_receivers_name())
        response.set_amount(deposit_request.get_amount())
        return response

    @staticmethod
    def map(login_request: LoginRequest):
        login_response = LoginResponse()
        login_response.set_account_number(login_request.get_account_number())
        return login_response
