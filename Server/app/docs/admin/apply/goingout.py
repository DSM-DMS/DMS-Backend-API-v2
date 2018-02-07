GOINGOUT_DOWNLOAD_GET = {
    'tags': ['신청 정보 관리'],
    'description': '외출신청 정보 다운로드',
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
            'description': '외출신청 정보 추출 성공. 엑셀 파일 응답',
            'examples': {
                'application/vnd.ms-excel': {
                    'PK\x03\x04\x14\x00\x00\x00..'
                }
            }
        },
        '403': {
            'description': '권한 없음'
        }
    }
}
