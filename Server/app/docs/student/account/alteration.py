CHANGE_PW_POST = {
    'tags': ['계정'],
    'description': '비밀번호 변경',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'currentPw',
            'description': '현재 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'newPw',
            'description': '바꿀 비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '비밀번호 변경 성공'
        },
        '403': {
            'description': '비밀번호 변경 실패(틀린 비밀번호), 또는 권한 없음'
        }
    }
}

CHANGE_NUMBER_POST = {
    'tags': ['계정'],
    'description': '학번 변경',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'newNumber',
            'description': '바꿀 학번',
            'in': 'json',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '학번 변경 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
