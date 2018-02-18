from binascii import hexlify
from hashlib import pbkdf2_hmac
from unittest import TestCase as TC
import ujson

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

    def _auth(self, auth_url_rule):
        res = self.client.post(
            auth_url_rule,
            data=ujson.dumps({'id': self.student_id if auth_url_rule == '/auth' else self.admin_id, 'pw': self.pw}),
            content_type='application/json'
        )

        return ujson.loads(res.data.decode())

    def _get_access_token(self, auth_url_rule='/auth'):
        resp = self._auth(auth_url_rule)

        return 'JWT ' + resp['accessToken']

    def _get_refresh_token(self, auth_url_rule='/auth'):
        resp = self._auth(auth_url_rule)

        return 'JWT ' + resp['refreshToken']

    def setUp(self):
        self._create_fake_accounts()
        self.admin_access_token = self._get_access_token('/admin/auth')
        self.student_access_token = self._get_access_token()
        self.admin_refresh_token = self._get_refresh_token('/admin/auth')
        self.student_refresh_token = self._get_refresh_token()

    def tearDown(self):
        AdminModel.objects.delete()
        StudentModel.objects.delete()
        # 마이그레이션 해야함

    def json_request(self, method, target_url_rule, data, token):
        """
        Helper for json request

        :type method: func
        :type target_url_rule: str
        :type data: dict or list
        :type token: str

        :return: response
        """
        return method(
            target_url_rule,
            data=ujson.dumps(data),
            content_type='application/json',
            headers={'Authorization': token}
        )
