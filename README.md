# DMS for DSM [![Build Status](https://travis-ci.org/DSM-DMS/DMS-Backend-API-v2.svg?branch=master)](https://travis-ci.org/DSM-DMS/DMS-Backend-API-v2) [![Coverage Status](https://coveralls.io/repos/github/DSM-DMS/DMS-Backend-API-v2/badge.svg)](https://coveralls.io/github/DSM-DMS/DMS-Backend-API-v2) [![works badge](https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)
Origin repository : <a href="https://github.com/DSM-DMS/DMS-Backend">DMS-Backend</a>

## 주 목표
- [x] JSON이 아닌 요청에 대해 400 Bad request를 돌려보내는 데코레이터 구현
- [x] API 접근 권한 관련 데코레이터 개선과 기존 API 전체에 적용
- [x] 요청 데이터를 받는 곳을 application/form-data나 application/x-www-form-urlencoded가 아닌 application/json으로 변경
- [ ] API의 request/response에서 key를 snake case에서 camel case로 변경(access_token to accessToken)
- [ ] JSON request가 필요한 API 각각에 대한 Swagger Model 정의
- [ ] Swagger doc 재구성
- [ ] 테스트 케이스 완전히 처음부터 개발
- [ ] Collection name과 collection 분할 방식 변경으로 인한 MongoDB Migrator 구현
- [ ] 유틸리티성 헬퍼 함수에 대한 docstring과 소스코드 전체에 대한 리팩토링, 주석처리
