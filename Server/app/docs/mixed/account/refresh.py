REFRESH_POST = {
    'tags': ['계정', '관리자 계정'],
    'description': '새로운 Access Token 획득',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Refresh Token(JWT ***)',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Refresh 성공. 새로운 Access Token 발급',
            'examples': {
                '': {
                    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlkZW50aXR5IjoiYSIsInR5cGUiOiJhY2Nlc3MiLCJleHAiOjE1NDA1NTc0NDYsImp0aSI6ImJiN2M3MjJmLTZkZjMtNDljYy1iZTk5LWRkMjMzNDU1NDRjZSIsIm5iZiI6MTUwOTAyMTQ0NiwiaWF0IjoxNTA5MDIxNDQ2fQ.wmytxSuQlH-KjhxO2EzrIioWHWgEnyiqWpRBwWuM15M'
                }
            }
        },
        '205': {
            'description': '로그인 실패(다른 디바이스에서 비밀번호가 변경됐거나, Refresh Token이 만료됨). '
                           '재로그인을 통한 새로운 Access Token과 Refresh Token 발급 필요'
        }
    }
}
