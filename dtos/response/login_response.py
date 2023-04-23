import decimal


class LoginResponse:

    def __init__(self):
        self.__full_name: str = ""
        self.__email: str = ""
        self.__phone_number: str = ""
        self.__account_balance: decimal = 0.00

    def set_full_name(self, full_name: str):
        self.__full_name = full_name

    def get_full_name(self) -> str:
        return self.__full_name

    def set_email(self, email: str):
        self.__email = email

    def get_email(self) -> str:
        return self.__email

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_account_balance(self, balance: decimal):
        self.__account_balance = balance

    def get_account_balance(self) -> decimal:
        return self.__account_balance
