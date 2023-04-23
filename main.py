import sys

from unicodedata import decimal

from controllers.account_controller import AccountController
from dtos.request.deposit_request import DepositRequest
from dtos.request.register_request import CreateAccountRequest

account_controller = AccountController()


def register():
    register_request = CreateAccountRequest()
    register_request.set_first_name(input("Enter First Name::: "))
    register_request.set_last_name(input("Enter Last Name::: "))
    register_request.set_phone_number(input("Enter Phone Number::: "))
    register_request.set_gmail(input("Enter Email Account::: "))
    register_request.set_password(input("Enter password::: "))

    result = account_controller.register(register_request)
    print(result.__str__())
    start_app()


def login():
    e_wallet_on_your_account()


def exit_app():
    sys.exit()


def send_money():
    deposit_request = DepositRequest()
    deposit_request.set_senders_name(input("Enter Sender's name::: "))
    deposit_request.set_receivers_account_number(input("Enter Account Number::: "))
    deposit_request.set_receivers_name(input("Enter Account Name::: "))
    deposit_request.set_amount(float(input("Enter Amount::: ")))
    deposit_request.set_purpose(input("Enter Narration::: "))

    result = account_controller.deposit(deposit_request)
    print(result.__str__())
    start_app()


def transactions():
    pass


def bank_statement():
    pass


def check_balance():
    result = account_controller.check_balance("8030669508")
    print(result.__str__())
    start_app()


def e_wallet_on_your_account():
    user_selection = int(input("""
    ==================
    1. Send Money
    2. Check Balance
    3. Transactions
    4. Print Bank Statement
    5. Exit App
    """))

    match user_selection:
        case 1:
            send_money()

        case 2:
            check_balance()

        case 3:
            transactions()

        case 4:
            bank_statement()

        case 5:
            exit_app()

        case _:
            start_app()


def start_app():
    user_input = int(input("""
    ===============
    1. Register
    2. Login
    3. Exit 
    ===============
    """))

    match user_input:
        case 1:
            register()

        case 2:
            login()

        case 3:
            exit_app()

        case _:
            start_app()


if __name__ == '__main__':
    start_app()
