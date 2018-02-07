# DMS for DSM [![Build Status](https://travis-ci.org/DSM-DMS/DMS-Backend-API-v2.svg?branch=master)](https://travis-ci.org/DSM-DMS/DMS-Backend-API-v2) [![Coverage Status](https://coveralls.io/repos/github/DSM-DMS/DMS-Backend-API-v2/badge.svg)](https://coveralls.io/github/DSM-DMS/DMS-Backend-API-v2) [![works badge](https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)
Origin repository : <a href="https://github.com/DSM-DMS/DMS-Backend">DMS-Backend</a>

## 주 목표
(x) 요청 데이터를 받는 곳을 application/form-data나 application/x-www-form-urlencoded가 아닌 application/json으로 변경
(x) request/response에서 JSON Object의 key를 snake case에서 camel case로 변경(access_token to accessToken)
(x) 테스트 케이스의 legacy 제거, Content-Type 변경
(x) Swagger doc을 모델 기반으로 변경
(x) Collection name과 collection 분할 방식 변경으로 인한 MongoDB Migrator 구현
