Festa.io 의 이벤트 목록 정렬하기
===================================

# 문제 설명

- 해나라는 Festa.io 에 그동안 다녀왔던 목록을 깃헙에 md 파일로 정리하고자 한다. 문제는 Festa의 내 티켓 목록에 나와있는 티켓이 시간순으로 정렬되어 있지 않을 뿐더러 이름/날짜/주최를 구분하기 위해서 한번 재정렬 할 필요가 있다는 것이다.

- 아래는 '내 티켓'에서 데이터를 긁어온 예시 이다.

```
2019년 12월 21일 오후 1:00
Android Dev Summit 2019 extended Seoul
GDG Korea Android
2018년 04월 22일 오전 9:00
DroidKnights
DroidKnights Community
2018년 06월 10일 오전 11:00
Google I/O Extended 2018 Seoul
GDG Korea
```

- 보시다시피 날짜, 행사이름, 주최자 순으로 세줄씩 나오고 이것이 반복 되는 것을 확인할 수 있다.
 
# 요구 사항

- 날짜, 행사이름, 주최자 순으로 출력되어있는 문자열을 입력 받았을 때, 날짜 순으로 원하는 포맷대로 출력할 수 있도록 하는 파이썬 프로그램 코드를 작성한다.

- 입력되는 포맷은 아래와 같다.
```
행사 일시
행사명
주최자 명
... 반복
```

- 해나라가 원하는 포맷은 아래와 같다.
```
### 행사명

- **⏰ 일시** : 행사 일시
- **💁 주최** : 주최자 명
... 반복
```

# 예제 입력

```
2019년 12월 21일 오후 1:00
Android Dev Summit 2019 extended Seoul
GDG Korea Android
2018년 04월 22일 오전 9:00
DroidKnights
DroidKnights Community
2018년 06월 10일 오전 11:00
Google I/O Extended 2018 Seoul
GDG Korea
```

# 예제 출력

```
### Android Dev Summit 2019 extended Seoul

- **⏰ 일시** : 2019. 12. 21 (토)
- **💁 주최** : GDG Korea Android

### Google I/O Extended 2018 Seoul

- **⏰ 일시** : 2018. 06. 10 (토)
- **💁 주최** : GDG Korea

### DroidKnights

- **⏰ 일시** : 2018. 04. 22 (토)
- **💁 주최** : DroidKnights Community
```

# 풀이

- 소스 코드 : [FestaListSorting.py](FestaListSorting.py)
- 입력받으면 3번에 한번씩 순서에 알맞게 맞추어 class에 넣은 다음 최종적으로 이벤트 목록을 날짜 역순으로 정렬하였다.

# 적용

- https://github.com/HaenaraShin/Dev-Conference-Review/commit/1209506e1080d3853f4ba591a73ebe2df2a5132d