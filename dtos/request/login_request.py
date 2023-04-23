import decimal


class LoginRequest:

    def __init__(self):
        self.__account_number: decimal = 0.00
        self.__password: str = ""

    def set_account_number(self, account_number: decimal):
        self.__account_number = account_number

    def get_account_number(self) -> decimal:
        return self.__account_number

    def set_password(self, password: str):
        self.__password = password

    def get_password(self) -> str:
        return self.__password
