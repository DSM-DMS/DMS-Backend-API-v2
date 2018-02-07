SURVEY_MANAGING_GET = {
    'tags': ['설문지 관리'],
    'description': '설문지 리스트 불러오기',
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
            'description': '설문지 리스트 불러오기 성공',
            'examples': {
                '': [
                    {
                        'id': 's3qldmc13opeflds',
                        'description': '치킨 어때?',
                        'creationTime': '2017-12-26',
                        'title': '내일 저녁 치킨먹기 찬반설문',
                        'startDate': '2017-10-24',
                        'endDate': '2017-10-25'
                    },
                    {
                        'id': '1fnfdj3391idkflds',
                        'description': '졸리다',
                        'creationTime': '2017-12-26',
                        'title': '등교 후 12시간 자습 찬반설문',
                        'startDate': '2017-10-24',
                        'endDate': '2017-10-30'
                    }
                ]
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

SURVEY_MANAGING_POST = {
    'tags': ['설문지 관리'],
    'description': '설문지 등록',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'description',
            'description': '설문지 설명',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '설문지 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'startDate',
            'description': '시작 날짜(YYYY-MM-DD)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'endDate',
            'description': '종료 날짜(YYYY-MM-DD)',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'target',
            'description': '대상 학년',
            'in': 'json',
            'type': 'list',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '설문지 등록 성공. 등록된 설문지의 ID 응답',
            'examples': {
                '': {
                    'id': '13211265df16ads'
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

SURVEY_MANAGING_DELETE = {
    'tags': ['설문지 관리'],
    'description': '설문지 삭제',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'surveyId',
            'description': '설문지 ID',
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '설문지 삭제 성공'
        },
        '204': {
            'description': '존재하지 않는 설문지 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

QUESTION_MANAGING_GET = {
    'tags': ['설문지 관리'],
    'description': '설문지 질문 리스트 불러오기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'surveyId',
            'description': '설문지 ID',
            'in': 'query',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': '질문 리스트 불러오기 성공',
            'examples': {
                '': [
                    {
                        'id': '13211265df16ads',
                        'title': '저녁에 치킨을 먹고 싶습니까?',
                        'isObjective': True,
                        'choicePaper': ['예', '아니오']
                    },
                    {
                        'id': '11265cd65432r9',
                        'title': '어디 치킨이 좋습니까?',
                        'isObjective': False
                    }
                ]
            }
        },
        '204': {
            'description': '존재하지 않는 설문지 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

QUESTION_MANAGING_POST = {
    'tags': ['설문지 관리'],
    'description': '설문지에 1개 이상의 질문 등록. title, is_objective, choice_paper는 "questions"에 JSONArray로 묶어 전송합니다.',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'surveyId',
            'description': '질문을 추가할 설문지 ID',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'title',
            'description': '질문 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'isObjective',
            'description': '객관식 여부',
            'in': 'json',
            'type': 'bool',
            'required': True
        },
        {
            'name': 'choicePaper',
            'description': '객관식 선택지',
            'in': 'json',
            'type': 'list',
            'required': False
        }
    ],
    'responses': {
        '201': {
            'description': '질문 추가 성공. 업로드된 질문의 ID 응답',
            'examples': {
                '': [
                    '13211265df16ads',
                    '13211265df16abc',
                    '13211265df16add',
                ]
            }
        },
        '204': {
            'description': '존재하지 않는 설문지 ID'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
