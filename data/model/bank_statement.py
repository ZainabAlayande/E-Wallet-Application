import decimal


class BankStatement:

    def __init__(self):
        self.__account_name: str = ""
        self.__account_number: str = ""
        self.__balance: decimal = 0.0

    def print_bank_statement(self):
        print("=============================================================================")
        print("================================ BANK OF ZEN ================================")
        print("                         MONTHLY ACCOUNT STATEMENT ")
        print("Account Name: ")
        print("Account Number: ")
        print("Bank Balance: ")
        print("Date: ")
        print("=============================================================================")
