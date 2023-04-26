import decimal

from data.model.account import Account
from data.repository.account_repository_impl import AccountRepositoryImpl
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from dtos.response.deposit_response import DepositResponse
from dtos.response.login_response import LoginResponse
from dtos.response.register_response import RegisterResponse
from dtos.response.transfer_response import TransferResponse
from dtos.response.withdraw_response import WithdrawResponse
from services.account_service import AccountService
from utils.account_not_found_exception import AccountNotFound
from utils.negative_amount_exception import CannotWithdrawNegativeAmount
from utils.mapper import Mapper
from utils.phone_number_exist_exception import PhoneNumberExist


class AccountServiceImpl(AccountService):
    account_repository = AccountRepositoryImpl()
    account = Account()

    def register_account(self, request: CreateAccountRequest) -> RegisterResponse:
        if self.phone_number_exist(request.get_phone_number()):
            raise PhoneNumberExist(request.get_phone_number() + " " + "already exist")

        account = Mapper.map_request_with_account(request)
        saved_account = self.account_repository.add(account)
        response = Mapper.map_account_with_response(saved_account)
        return response

    def phone_number_exist(self, phone_nuber):
        phone_nuber = self.account_repository.find_phone_number(phone_nuber)
        if phone_nuber is not None:
            return True
        return False

    def login(self, login_request: LoginRequest) -> LoginResponse:
        if not self.account_repository.find_by_account_number(login_request.get_account_number()):
            raise AccountNotFound("Account not found..")

        login_response = Mapper.map(login_request)
        return login_response

    def deposit_into(self, deposit_request: DepositRequest) -> str:
        account = self.account_repository.find_by_account_number(deposit_request
                                                                 .get_receivers_account_number())
        if not account:
            raise AccountNotFound("Account not found.")

        self.validate_negative_amount(deposit_request.get_amount())
        account.deposit(deposit_request.get_amount())
        self.account_repository.add(account)
        print()
        return "Successfully deposited."

    def withdraw_from(self, withdraw_request: WithdrawRequest) -> WithdrawResponse:
        account = self.account_repository.find_by_account_number(withdraw_request
                                                                 .get_account_number())
        if not account:
            raise AccountNotFound("Account not found..")

        self.validate_negative_amount(withdraw_request.get_amount())
        account.withdraw(withdraw_request.get_amount())
        self.account_repository.add(account)
        withdraw_response = WithdrawResponse()
        return withdraw_response

    @staticmethod
    def validate_negative_amount(amount: decimal):
        if amount < 0:
            return "Negative amount not valid."

    def check_balance(self, account_number: str) -> decimal:
        account = self.account_repository.find_by_account_number(account_number)
        if not account:
            raise AccountNotFound("Account not found..")

        return account.get_balance()

    def account_not_found(self, account):
        account_number = self.account_repository.find_by_account_number(account)
        if account_number is not None:
            return True
        return False

    def transfer(self, transfer_request: TransferRequest) -> TransferResponse:
        if self.account_not_found(transfer_request.get_receiver_account_number() and
                                  transfer_request.get_sender_account_number()):
            raise AccountNotFound("Account not found..")

        withdraw_request = WithdrawRequest()
        withdraw_request.set_account_number(transfer_request.get_sender_account_number())
        withdraw_request.set_amount(transfer_request.get_amount())
        self.withdraw_from(withdraw_request)

        deposit_request = DepositRequest()
        deposit_request.set_receivers_account_number(transfer_request.get_receiver_account_number())
        deposit_request.set_amount(transfer_request.get_amount())
        self.deposit_into(deposit_request)

        transfer_response = TransferResponse()
        return transfer_response
