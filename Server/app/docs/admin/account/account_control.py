ACCOUNT_CONTROL_POST = {
    'tags': ['관리자 계정'],
    'description': '계정 삭제 후 새로운 UUID 생성',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'number',
            'description': '학번',
            'in': 'formData',
            'type': 'int',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '계정 삭제, UUID 생성 성공',
            'examples': {
                'application/json': {
                    'uuid': '022d'
                }
            }
        },
        '204': {
            'description': '해당 학번에 해당하는 학생이 없음'
        },
        '205': {
            'description': 'UUID가 이미 생성되었으며, 가입되지 않은 상태'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

ACCOUNT_CONTROL_DELETE = {
    'tags': ['관리자 계정'],
    'description': '관리자 계정 삭제',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '삭제할 관리자 계정 id',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '계정 삭제 성공'
        },
        '204': {
            'description': '존재하지 않는 관리자 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}