from unittest import TestCase

from InstantPay.dtos.request.request_class import CreateAccountRequest
from InstantPay.services.account_serviceImpl import AccountServiceImpl


class TestAccountServiceImpl(TestCase):

    def test_register_account(self):
        account_service = AccountServiceImpl()
        request = CreateAccountRequest()
        request.set_first_name("sunday")
        request.set_last_name("emmanuel")
        request.set_phone_number("09152652431")
        request.set_pin("2796")

        expected = """
         Account Number: 9152652431,
         Full Name: sunday emmanuel,
         Balance: 0.0"""
        self.assertEqual(expected, account_service.register_account(request).__str__())

    def test_login(self):
        request = CreateAccountRequest()
        request.set_phone_number("09152652431")
        request.set_password("sunday")
        request.set_first_name("sunday")
        request.set_last_name("emma")
        account_service = AccountServiceImpl()
        account_service.register_account(request)
        self.assertTrue(account_service.login("9152652431", "sunday"))

    def test_deposit(self):
        request = CreateAccountRequest()
        request.set_phone_number("09152652431")
        request.set_password("sunday")
        request.set_first_name("sunday")
        request.set_last_name("emma")
        account_service = AccountServiceImpl()
        account_service.register_account(request)
        account_service.deposit("9152652431", 300.0)
        self.assertEqual(300.0, account_service.check_balance("9152652431"))

    def test_withdraw(self):
        request = CreateAccountRequest()
        request.set_phone_number("09152652431")
        request.set_password("sunday")
        request.set_first_name("sunday")
        request.set_last_name("emma")
        account_service = AccountServiceImpl()
        account_service.register_account(request)
        account_service.deposit("9152652431", 300.0)
        account_service.withdraw("9152652431", 200)
        self.assertEqual(100.0, account_service.check_balance("9152652431"))

    def test_transfer(self):
        request = CreateAccountRequest()
        request.set_phone_number("09152652431")
        request.set_password("sunday")
        request.set_first_name("sunday")
        request.set_last_name("emma")
        account_service = AccountServiceImpl()
        account_service.register_account(request)
        account_service.deposit("9152652431", 300.0)

        request.set_phone_number("08134132226")
        request.set_password("bright")
        request.set_first_name("sunepa")
        request.set_last_name("tomiwa")
        account_service = AccountServiceImpl()
        account_service.register_account(request)
        account_service.transfer("9152652431", "8134132226", 200.0)
        self.assertEqual(100.0, account_service.check_balance("9152652431"))
        self.assertEqual(200.0, account_service.check_balance("8134132226"))