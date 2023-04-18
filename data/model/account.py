class Account:

    def __init__(self, account_number: int, first_name: str, last_name: str, phone_number: str, pin: str):
        self.balance = None
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__pin = pin

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

    def get_gmail(self) -> str:
        return self.__pin

    def set_gmail(self, pin):
        self.__pin = pin
