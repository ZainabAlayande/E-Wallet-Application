import smtplib
import ssl
from email.message import EmailMessage
from unittest import TestCase

from data.model.mail_sender import MailSender
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from services.account_serviceImpl import AccountServiceImpl
from utils.phone_number_exist_exception import PhoneNumberExist


class TestAccountServiceImpl(TestCase):

    def test_account_can_be_registered(self):
        account_service = AccountServiceImpl()
        request = CreateAccountRequest()
        mail_sender = MailSender()

        request.set_first_name("sunday")
        request.set_last_name("emmanuel")
        request.set_gmail("sunday-emmanuel@gmail.com")
        request.set_phone_number("08023677114")
        request.set_password("password")
        request.set_account_number(request.get_account_number())

        subject_in = ""
        body_in = ""
        to_in = ""
        msg_sender = 'instantpay529@gmail.com'
        msg_password = 'ygcizpgdipolnkgc'
        msg_receiver2 = to_in
        subject = subject_in
        body = body_in

        em = EmailMessage()
        em['From'] = msg_sender
        em['To'] = msg_receiver2
        em['Subject'] = subject
        em.set_content(body)

        content = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=content) as smtp:
            smtp.login(msg_sender, msg_password)
            smtp.sendmail(msg_sender, msg_receiver2, em.as_string())

        mail_sender.email_alert("Account Registration", """
        Congratulations! 
        You have successfully created
        an account with instant pay e_wallet
        """, request.get_gmail())
        expected = """
         Account Number: 8023677114
         Gmail: sunday-emmanuel@gmail.com
         Full Name: sunday emmanuel
         Balance: 0.0"""
        self.assertEqual(expected, account_service.register_account(request).__str__())

    def test_register_with_same_phone_number_throw_exception(self):
        account_service = AccountServiceImpl()
        register_request = CreateAccountRequest()

        register_request.set_phone_number("09045788992")
        account_service.register_account(register_request)

        register_request.set_phone_number("09045765992")
        account_service.register_account(register_request)
        with self.assertRaises(PhoneNumberExist):
            account_service.register_account(register_request)

    def test_user_can_login_in(self):
        request = CreateAccountRequest()
        request.set_phone_number("08198765432")
        request.set_password("password")
        request.set_first_name("Austin")
        request.set_last_name("Barbel")
        request.set_gmail("austin-barbel@gmail.com")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        login_request = LoginRequest()
        login_request.set_account_number("8198765432")
        login_request.set_password("password")
        self.assertTrue(account_service.login(login_request))

    def test_money_can_be_deposited(self):
        request = CreateAccountRequest()
        request.set_phone_number("09152652431")
        request.set_password("password")
        request.set_first_name("Sunday")
        request.set_last_name("Emma")
        request.set_gmail("emma-sunday@gmail.com")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        deposit_request = DepositRequest()
        deposit_request.set_senders_name("Divine Grace")
        deposit_request.set_receivers_account_number("9152652431")
        deposit_request.set_receivers_name(request.get_first_name() + " " + request.get_last_name())
        deposit_request.set_amount(4000.0)
        account_service.deposit_into(deposit_request)

        deposit_request.set_amount(4000.0)
        account_service.deposit_into(deposit_request)
        self.assertEqual(8000.0, account_service.check_balance("9152652431"))

        # expected = """
        #     Senders Name: Divine Grace
        #     Receivers Account: 9152652431
        #     Receivers Name: Sunday Emma
        #     Balance: 4345.0"""
        # self.assertEqual(expected, account_service.deposit_into(deposit_request).__str__())

    def test_deposit_negative_amount_balance_is_equal_to_original_balance(self):
        request = CreateAccountRequest()
        request.set_phone_number("08123455667")
        request.set_pin(7865)
        request.set_first_name("sunday")
        request.set_last_name("emma")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        deposit_request = DepositRequest()
        deposit_request.set_receivers_account_number("8123455667")
        deposit_request.set_amount(100.0)
        account_service.deposit_into(deposit_request)

        deposit_request.set_amount(-30000.0)
        account_service.deposit_into(deposit_request)

        self.assertEqual(100.0, account_service.check_balance("8123455667"))

    def test_money_can_be_withdrawn(self):
        request = CreateAccountRequest()
        request.set_phone_number("08030669508")
        request.set_password("password")
        request.set_first_name("Sunday")
        request.set_last_name("Emma")
        request.set_gmail("sunday-email@gmail.com")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        deposit_request = DepositRequest()
        deposit_request.set_receivers_account_number("8030669508")
        deposit_request.set_amount(5000.00)

        account_service.deposit_into(deposit_request)

        withdraw_request = WithdrawRequest()
        withdraw_request.set_account_number("8030669508")
        withdraw_request.set_amount(1000.0)

        account_service.withdraw_from(withdraw_request)
        self.assertEqual(4000.0, account_service.check_balance("9152652431"))

    def test_money_can_be_transferred(self):
        # account 1
        request = CreateAccountRequest()
        request.set_phone_number("08181587649")
        request.set_password("password")
        request.set_first_name("Sunday")
        request.set_last_name("Emma")
        request.set_gmail("emma-sunday@gmail.com")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        deposit_request = DepositRequest()
        deposit_request.set_receivers_account_number("8181587649")
        deposit_request.set_amount(10000.0)
        account_service.deposit_into(deposit_request)

        # assert account one balance is 10000
        self.assertEqual(10000.00, account_service.check_balance("8181587649"))

        withdraw_request = WithdrawRequest()
        withdraw_request.set_account_number("8181587649")
        withdraw_request.set_amount(2000.0)

        account_service.withdraw_from(withdraw_request)
        self.assertEqual(8000.0, account_service.check_balance("9152652431"))

        # account two
        request_two = CreateAccountRequest()
        request_two.set_phone_number("070123456778")
        request_two.set_password("password")
        request_two.set_first_name("Monday")
        request_two.set_last_name("Julius")
        request_two.set_gmail("monday-julius@gmail.com")

        account_service = AccountServiceImpl()
        account_service.register_account(request_two)

        # assert that account two is 0
        self.assertEqual(0.00, account_service.check_balance("70123456778"))

        transfer_request = TransferRequest()
        transfer_request.set_sender_account_number("8181587649")
        transfer_request.set_amount(2000.0)

        transfer_request.set_receiver_account_number("70123456778")

        self.assertEqual(8000.0, account_service.check_balance("8181587649"))
        self.assertEqual(2000.0, account_service.check_balance("70123456778"))
