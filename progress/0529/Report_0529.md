# 5월 29일
---
#### 1. 진행상황
* 마피아 로직 구현: 서순호
* 글, 댓글 삭제 프런트: 김효민
* 해시태그 프런트 진행중: 장유원
* 해시태그 백엔드: 최원석
* 해시태그 백엔드 테스트: 김효민
* 효과음: 최원석
* 엔터로 로그인, 회원가입과 채팅 가능: 서순호

* 원래 다른 작업을 하려했지만 마피아 작업을 먼저 하는것이 좋다고 생각하였습니다. 따라서 마피아 로직을 먼저 시작하였습니다.

* 그리고 해시태그 작업과 효과음을 먼저 하기로 하엿습니다.

#### 2. 백엔드 추가 API 스펙
| Url | Description | Example
| --- | --- | --- |
| GET `/hashtag/` | 모든 글에 존재하는 해시태그를 받아온다. | hashtags:[ht1, ht2] |
 GET `/hashtag/<tagname>` | 해당 tagname의 해시태그가 들어있는 feedid의 리스트를 받아온다. | id: [12, 15]
* `python3 runtest_back.py`

#### 3. 프런트엔드 테스트 코드
* `python3 runtest_front.py`

#### 4. Redux unit test
* `frontend/jest` 에 존재합니다.

#### 5. aws 링크
* 13.124.80.116:3000 프런트엔드
* 13.124.80.116:8000 백엔드