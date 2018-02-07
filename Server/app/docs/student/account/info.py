MYPAGE_GET = {
    'tags': ['계정'],
    'description': '마이페이지 정보 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '마이페이지 조회 성공',
            'examples': {
                'application/json': {
                    'name': '조민규',
                    'number': 20120,
                    'extension11': {
                        'classNum': 2,
                        'seatNum': 13
                    },
                    'extension12': None,
                    'goingout': {
                        'sat': True,
                        'sun': False
                    },
                    'stayValue': 4,
                    'goodPoint': 1,
                    'badPoint': 458756945
                }
            }
        },
        '403': {
            'description': '권한 없음(재로그인 필요)'
        }
    }
}
