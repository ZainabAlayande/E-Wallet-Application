import sys

from unicodedata import decimal

from controllers.account_controller import AccountController
from controllers.complain_controller import ComplainController
from dtos.request.complain_request import ComplainRequest
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from utils.time import ClassTime

login_request = LoginRequest()
complain_controller = ComplainController()
account_controller = AccountController()
delay_program = ClassTime()


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
        print()
        print(result.__str__())
        if result == "Account not found":
            self.start_app()
        else:
            self.__current_user_logged_in = login_request.get_account_number()
            self.e_wallet_on_your_account()

    def exit_app(self):
        sys.exit()

    def deposit_money(self):
        deposit_request = DepositRequest()
        print("Enter Account Details: ")
        deposit_request.set_amount(float(input("Enter Amount::: ")))
        deposit_request.set_purpose(input("Enter Narration::: "))
        deposit_request.set_receivers_account_number(input("Enter Account Number::: "))
        delay_program.delay()
        print()

        # account_controller.transfer(transfer_request)
        # print("Receivers Account Name::: ", transfer_request.get_receiver_account_name())
        # user_input = input("""
        #        **Confirm receivers account name:::
        #                1 -> OK
        #                2 -> NOT OK""")

        result = account_controller.deposit(deposit_request)
        print("Account Name: ", deposit_request.get_receivers_account_name())

        print(result.__str__())
        self.e_wallet_on_your_account()

    def transactions(self):
        self.e_wallet_on_your_account()

    def bank_statement(self):
        self.e_wallet_on_your_account()

    def check_balance(self):
        print()
        result = account_controller.check_balance(self.__current_user_logged_in)
        print("Balance: ", result.__str__())
        self.e_wallet_on_your_account()

    def e_wallet_on_your_account(self):
        user_selection = input("""
        ==================
        1. Send Money
        2. Deposit
        3. Check Balance
        4. Print Bank Statement
        5. Help Desk
        6. Track Complaint Status
        7. Log out
        8. Exit App
        """)

        self.validate_empty_string_cannot_break_code(user_selection)

        match user_selection:
            case "1":
                self.transfer_money()

            case "2":
                self.deposit_money()

            case "3":
                self.check_balance()

            case "4":
                self.bank_statement()

            case "5":
                self.log_complain()

            case "6":
                self.check_complain_status()

            case "7":
                self.start_app()

            case "8":
                self.exit_app()

            case _:
                self.start_app()

    def start_app(self):
        user_input = input("""
        ===============
        1. Register
        2. Login
        3. Exit 
        ===============
        """)

        self.validate_empty_string_cannot_break_code(user_input)

        match user_input:
            case "1":
                self.register()

            case "2":
                self.login()

            case "3":
                self.exit_app()

            case _:
                self.start_app()

    def validate_empty_string_cannot_break_code(self, empty: str):
        empty_string = ""
        if empty == empty_string:
            print("Input can not be empty")

    def success_message(self) -> str:
        return "Transfer Successful"

    # def withdraw(self):
    #     withdraw_request = WithdrawRequest()
    #     withdraw_request.set_account_number(input("Enter your account number: "))
    #     withdraw_request.set_amount(float(input("Enter amount: ")))
    #     result = account_controller.withdraw(withdraw_request)
    #
    #     print(result.__str__())
    #     self.e_wallet_on_your_account()

    def transfer_money(self):
        transfer_request = TransferRequest()
        transfer_request.set_sender_account_number(self.__current_user_logged_in)
        print("Current user logged in and senders account -> ", self.__current_user_logged_in)
        transfer_request.set_amount(float(input("Enter amount to send::: ")))
        transfer_request.set_receiver_account_number(input("Enter receiver's account number::: "))
        print()
        delay_program.delay()
        account_controller.transfer(transfer_request)
        print()
        print("Receivers Account Name::: ", transfer_request.get_receiver_account_name())

        # user_input = input("""
        # **Confirm receivers account name:::
        #         1 -> OK
        #         2 -> NOT OK
        #         """)
        # self.validate_empty_string_cannot_break_code(user_input)
        #
        # match user_input:
        #     case "1":
        #         self.success_message()
        #     case "2":
        #         self.e_wallet_on_your_account()
        #     case _:
        #         self.start_app()

        self.e_wallet_on_your_account()

    def log_complain(self):
        complain_request = ComplainRequest()
        complain_request.set_user_full_name(input("Enter full name::: "))
        complain_request.set_user_email_address(input("Provide email address::: "))
        complain_request.set_title_of_complain(input("Enter suitable title for your complain::: "))
        complain_request.set_body_of_complain(input("Provide details of complain::: "))
        delay_program.delay_for_logging_request()
        result = complain_controller.log_complain(complain_request)

        print(result.__str__())
        self.e_wallet_on_your_account()

    def check_complain_status(self):
        identity_number = int(input("Enter identity_number::: "))
        result = complain_controller.check_complaint_status(identity_number)
        print(result.__str__())
        self.e_wallet_on_your_account()


if __name__ == '__main__':
    my_object = main()
    my_object.start_app()
