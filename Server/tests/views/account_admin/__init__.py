from binascii import hexlify
from hashlib import pbkdf2_hmac
import json

from app import app

from app.models.account import AdminModel


def create_fake_account(id='fake_admin'):
    pw = hexlify(
        pbkdf2_hmac(
            hash_name='sha256',
            password=b'fake',
            salt=app.secret_key.encode(),
            iterations=100000
        )
    ).decode('utf-8')

    AdminModel(
        id=id,
        pw=pw,
        name='fake'
    ).save()


def remove_fake_account(id='fake_admin'):
    AdminModel.objects(
        id=id
    ).delete()


def get_access_token(client, id='fake_admin', pw='fake'):
    res = client.post('/admin/auth', data=json.dumps({'id': id, 'pw': pw}), content_type='application/json')

    return 'JWT ' + json.loads(res.data.decode())['accessToken']


def get_refresh_token(client, id='fake_admin', pw='fake'):
    res = client.post('/admin/auth', data=json.dumps({'id': id, 'pw': pw}), content_type='application/json')

    return 'JWT ' + json.loads(res.data.decode())['refreshToken']
