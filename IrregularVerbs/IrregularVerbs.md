Irregular Verbs 퀴즈 만들기
========================

# 문제 설명
- 기수는 요즘 영어 공부를 하고 있다. 그 중에서 불규칙 동사 변화형을 공부하는데
  어려움이 많다. 이를 해결 하기 위해 퀴즈 프로그램을 만들려고 한다.

|  infinitive  |  simple past  |  past participle  |  meaning in KOR  |
|--------------|---------------|-------------------|------------------|
|<center>be</center>|<center>was/were</center>|<center>been</center>|<center>~이다.</center>|
|--------------|---------------|-------------------|------------------|
|<center>bear</center>|<center>bore</center>|<center>born</center>|<center>(새끼를) 낳다.</center>|
|--------------|---------------|-------------------|------------------|
|<center>...</center>|<center>...</center>|<center>...</center>|<center>...</center>|

- 위의 예를 보면 불규칙 동사 변화형은 현재, 과거, 과거분사, 뜻으로 이루어져 있다.
- 전체 표에서 중간 중간 빈칸이 생기게 한다.
  
# 요구 사항
- 일일히 입력하기 번거롭다. 그러므로 파일의 이름을 입력 받아 해당 파일의 내용을 읽기로 한다.
  입력 포맷은 다음과 같다.
```
IrregularVerbs.txt

be|was/were|been|~이다.
bear|bore|born|(새끼를)낳다.
...반복
```
- 뜻은 항상 보여주고 infinitive, simple past, past participle 중 하나가 빈칸이 되게 한다.
- 기수가 원하는 출력 포맷은 다음과 같다.
```
be - (    ) - been - ~이다 : 정답입력
(    ) - bore - born - (새끼를)낳다. : 정답입력
...반복(그만하고 싶을 경우 'Q' 입력)
```
# 풀이
- 소스코드 [Irregular.Verbs](IrregularVerbs.py)에 작업중...