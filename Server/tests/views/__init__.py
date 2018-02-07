from binascii import hexlify
from hashlib import pbkdf2_hmac
from unittest import TestCase as TC
import json

from tests.views import account_admin, account_student
from app import app
from app.models.account import AdminModel, StudentModel


class TCBase(TC):
    def __init__(self, *args, **kwargs):
        TC.__init__(self, *args, **kwargs)

        self.client = app.test_client()
        self.admin_id = 'fake_admin'
        self.student_id = 'fake_student'
        self.pw = 'fake'
        self.hashed_pw = hexlify(
            pbkdf2_hmac(
                hash_name='sha256',
                password=self.pw.encode(),
                salt=app.secret_key.encode(),
                iterations=100000
            )
        ).decode('utf-8')

    def _create_fake_accounts(self):
        AdminModel(
            id=self.admin_id,
            pw=self.hashed_pw,
            name='fake'
        ).save()

        StudentModel(
            id=self.student_id,
            pw=self.hashed_pw,
            name='fake',
            number=1111
        ).save()

    def _get_access_token(self, auth_rul_rule='/auth'):
        res = self.client.post(
            auth_rul_rule,
            data=json.dumps({'id': self.student_id if auth_rul_rule == '/auth' else self.admin_id, 'pw': self.pw}),
            content_type='application/json'
        )

        return 'JWT ' + json.loads(res.data.decode())['accessToken']

    def _get_refresh_token(self, refresh_rul_rule='/refresh'):
        res = self.client.post(
            refresh_rul_rule,
            data=json.dumps({'id': self.student_id if refresh_rul_rule == '/refresh' else self.admin_id, 'pw': self.pw}),
            content_type='application/json'
        )

        return 'JWT ' + json.loads(res.data.decode())['refreshToken']

    def setUp(self):
        self._create_fake_accounts()
        self.admin_access_token = self._get_access_token('/admin/auth')
        self.student_access_token = self._get_access_token()

    def tearDown(self):
        AdminModel.objects.delete()
        StudentModel.objects.delete()
        # 마이그레이션 해야함
