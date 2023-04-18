from unittest import TestCase

from data.model.account import Account
from data.repository.account_repository_impl import AccountRepositoryImpl


class TestAccountRepositoryImpl(TestCase):

    def test_save_one_account_count_is_one(self):
        account_repository = AccountRepositoryImpl()
        account = Account(1, "zainab", "blessing", "09078966554", "1234")
        account_repository.add(account)
        self.assertEqual(1, account_repository.count())

    def test_save_three_account_count_is_three(self):
        account_repository = AccountRepositoryImpl()
        account = Account(1, "zainab", "blessing", "09078966554", "9807")
        account_two = Account(2, "felix", "cindy", "08134566778", "5673")
        account_three = Account(3, "zainab", "blessing", "07089543215", "7786")

        account_repository.add(account)
        account_repository.add(account_two)
        account_repository.add(account_three)
        self.assertEqual(3, account_repository.count())

    # def test_save_one_account_count_is_one(self):
    #     account_repository = AccountRepositoryImpl()
    #     account = Account(1, "zainab", "blessing", "09078966554", "1234")
    #     account_repository.add(account)
    #     self.assertEqual(1, account_repository.count())



    # def test_save_three_account_delete_one_count_is_two(self):
    #     account_repository = AccountRepositoryImpl()
    #     account = Account("zainab", "blessing", "09078966554", 9807)
    #     account_two = Account("felix", "cindy", "08134566778", 5673)
    #     account_three = Account("zainab", "blessing", "07089543215", "3456")
    #
    #     account_repository.add(account)
    #     account_repository.add(account_two)
    #     account_repository.add(account_three)
    #     account_repository.delete(1)
    #     self.assertEqual(2, account_repository.count())
    #

