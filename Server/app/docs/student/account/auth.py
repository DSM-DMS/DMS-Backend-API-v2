AUTH_POST = {
    'tags': ['계정'],
    'description': '로그인',
    'parameters': [
        {
            'name': 'id',
            'description': 'ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'pw',
            'description': '비밀번호',
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '로그인 성공',
            'examples': {
                '': {
                    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlkZW50aXR5IjoiYSIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE1NDA1NTc0NDYsImp0aSI6ImJiN2M3MjJmLTZkZjMtNDljYy1iZTk5LWRkMjMzNDU1NDRjZSIsIm5iZiI6MTUwOTAyMTQ0NiwiaWF0IjoxNTA5MDIxNDQ2fQ.wmytxSuQlH-KjhxO2EzrIioWHWgEnyiqWpRBwWuM15M',
                    'refreshToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MTM5MDQ3NjMsImlkZW50aXR5IjoibmlsIiwiZnJlc2giOmZhbHNlLCJqdGkiOiI1Yzg1ZDAxNy1lYjIwLTRmYjgtYmVhYi1iYmYyZTQyY2NlYmYiLCJuYmYiOjE1MTM2NDU1NjMsInR5cGUiOiJhY2Nlc3MiLCJpYXQiOjE1MTM2NDU1NjN9.075C0_-b-oqSWc-jz7G35y00erRVntpcqN9uMIAnvfI'
                }
            }
        },
        '401': {
            'description': '로그인 실패'
        }
    }
}

AUTH_CHECK_GET = {
    'tags': ['계정'],
    'description': '로그인 상태 체크',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '로그인되어 있음'
        },
        '401': {
            'description': '로그인되어 있지 않음'
        },
        '403': {
            'description': '학생 계정이 아님'
        }
    }
}
