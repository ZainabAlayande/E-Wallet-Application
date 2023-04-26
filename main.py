import sys

from unicodedata import decimal

from controllers.account_controller import AccountController
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.withdraw_request import WithdrawRequest

login_request = LoginRequest()
account_controller = AccountController()


class main:

    def __init__(self):
        self.__current_user_logged_in = ""

    def register(self):
        register_request = CreateAccountRequest()
        register_request.set_first_name(input("Enter First Name::: "))
        register_request.set_last_name(input("Enter Last Name::: "))
        register_request.set_phone_number(input("Enter Phone Number::: "))
        register_request.set_gmail(input("Enter Email Account::: "))
        register_request.set_password(input("Enter password::: "))

        result = account_controller.register(register_request)
        print(result.__str__())
        self.start_app()

    def login(self):
        login_request.set_account_number(input("Enter account number::: "))
        login_request.set_password(input("Enter password::: "))
        result = account_controller.login(login_request)
        print(result.__str__())
        self.__current_user_logged_in = login_request.get_account_number()
        self.e_wallet_on_your_account()

    def exit_app(self):
        sys.exit()

    def send_money(self):
        deposit_request = DepositRequest()
        deposit_request.set_senders_name(input("Enter Sender's name::: "))
        deposit_request.set_receivers_account_number(input("Enter Account Number::: "))
        deposit_request.set_receivers_name(input("Enter Account Name::: "))
        deposit_request.set_amount(float(input("Enter Amount::: ")))
        deposit_request.set_purpose(input("Enter Narration::: "))

        result = account_controller.deposit(deposit_request)
        print(result.__str__())
        self.e_wallet_on_your_account()

    def transactions(self):
        pass

    def bank_statement(self):
        pass

    def check_balance(self):
        print()
        result = account_controller.check_balance(self.__current_user_logged_in)
        print("Balance: ", result.__str__())
        self.e_wallet_on_your_account()

    def e_wallet_on_your_account(self):
        user_selection = int(input("""
        ==================
        1. Send Money
        2. Withdraw
        3. Check Balance
        4. Transactions
        5. Print Bank Statement
        6. Go Back <-
        7. Exit App
        """))

        match user_selection:
            case 1:
                self.send_money()

            case 2:
                self.withdraw()

            case 3:
                self.check_balance()

            case 4:
                self.transactions()

            case 5:
                self.bank_statement()

            case 6:
                self.start_app()

            case 7:
                self.exit_app()

            case _:
                self.start_app()

    def start_app(self):
        user_input = int(input("""
        ===============
        1. Register
        2. Login
        3. Exit 
        ===============
        """))

        match user_input:
            case 1:
                self.register()

            case 2:
                self.login()

            case 3:
                self.exit_app()

            case _:
                self.start_app()

    def withdraw(self):
        withdraw_request = WithdrawRequest()
        withdraw_request.set_account_number(input("Enter your account number: "))
        withdraw_request.set_amount(float(input("Enter amount: ")))
        result = account_controller.withdraw(withdraw_request)

        print(result.__str__())
        self.e_wallet_on_your_account()


if __name__ == '__main__':
    my_object = main()
    my_object.start_app()
