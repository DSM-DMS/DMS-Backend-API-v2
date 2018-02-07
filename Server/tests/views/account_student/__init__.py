from binascii import hexlify
from hashlib import pbkdf2_hmac
import json

from app import app

from app.models.account import StudentModel


def create_fake_account(id='fake_student'):
    pw = hexlify(
        pbkdf2_hmac(
            hash_name='sha256',
            password=b'fake',
            salt=app.secret_key.encode(),
            iterations=100000
        )
    ).decode('utf-8')

    StudentModel(
        id=id,
        pw=pw,
        name='fake',
        number=1111
    ).save()


def remove_fake_account(id='fake_student'):
    StudentModel.objects(
        id=id
    ).delete()


def get_access_token(client, id='fake_student', pw='fake'):
    res = client.post('/auth', data=json.dumps({'id': id, 'pw': pw}), content_type='application/json')

    return 'JWT ' + json.loads(res.data.decode())['accessToken']


def get_refresh_token(client, id='fake_student', pw='fake'):
    res = client.post('/auth', data=json.dumps({'id': id, 'pw': pw}), content_type='application/json')

    return 'JWT ' + json.loads(res.data.decode())['refreshToken']
