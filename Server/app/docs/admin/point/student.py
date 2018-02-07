STUDENT_MANAGING_GET = {
    'tags': ['상벌점 관리'],
    'description': '학생 목록 조회',
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
            'description': '목록 조회 성공. 학번 기준으로 오름차순 정렬됩니다.',
            'examples': {
                '': [
                    {
                        'id': 'city7310',
                        'name': '조민규',
                        'number': 2120,
                        'goodPoint': 1,
                        'badPoint': 50,
                        'pointHistories': [
                            {
                                'time': '2018-01-01 12:34:12',
                                'reason': '치킨 먹음',
                                'point': 4
                            },
                            {
                                'time': '2018-01-02 12:34:12',
                                'reason': '이유 없음',
                                'point': -3
                            }
                        ],
                        'penaltyTrainingStatus': 4
                    },
                    {
                        'id': 'geni429',
                        'name': '정근철',
                        'number': 2117,
                        'goodPoint': 0,
                        'badPoint': 0,
                        'pointHistories': [
                            {
                                'time': '2018-01-01 12:34:12',
                                'reason': '치킨 먹음',
                                'point': 4
                            },
                            {
                                'time': '2018-01-02 12:34:12',
                                'reason': '이유 없음',
                                'point': -3
                            }
                        ],
                        'penaltyTrainingStatus': 0
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
