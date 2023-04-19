class Account:

    def __init__(self):
        self.__id: int = 0
        self.__balance: float = 0.0
        self.__account_number: str = ""
        self.__first_name: str = ""
        self.__last_name: str = ""
        self.__phone_number: str = ""
        self.__pin: str = ""
        self.__password: str = ""

    def get_first_name(self) -> str:
        return self.__first_name

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def get_pin(self) -> str:
        return self.__pin

    def set_pin(self, pin: str):
        self.__pin = pin

    def get_account_number(self) -> str:
        return self.__account_number

    def set_account_number(self, number):
        self.__account_number = number

    def set_password(self, password: str):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_id(self, identity_number: int):
        self.__id = identity_number

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount
