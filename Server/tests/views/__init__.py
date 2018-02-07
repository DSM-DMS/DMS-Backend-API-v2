from unittest import TestCase as TC

from tests.views import account_admin, account_student
from app import app


class TCBase(TC):
    def __init__(self):
        TC.__init__(self)

        self.client = app.test_client()

    def setUp(self):
        account_admin.create_fake_account()
        account_student.create_fake_account()
        self.admin_access_token = account_admin.get_access_token(self.client)
        self.student_access_token = account_student.get_access_token(self.client)

    def tearDown(self):
        account_admin.remove_fake_account()
        account_student.remove_fake_account()
