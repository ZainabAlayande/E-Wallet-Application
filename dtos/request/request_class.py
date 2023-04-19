class CreateAccountRequest:

    def __init__(self, ):
        self.balance = 0.00
        self.__account_number = None
        self.__first_name = None
        self.__last_name = None
        self.__phone_number = None
        self.__pin = None
        self.__password = None

    def get_first_name(self) -> str:
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_pin(self) -> str:
        return self.__pin

    def set_pin(self, pin):
        self.__pin = pin

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number: int):
        self.__account_number = account_number

    def get_password(self):
        return self.__password

    def set_password(self, password: str):
        self.__password = password

