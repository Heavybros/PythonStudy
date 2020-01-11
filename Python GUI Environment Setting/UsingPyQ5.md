파이썬으로 GUI 프로그래밍 환경구성💡
==========================
__본 문서는 아래의 OS, 및 개발환경을 사용합니다.__
__OS : Windows 10 64bit__
__개발도구 : vscode, Qt-Designer__
* * *
PyQt5 설치 방법
-----------
PyQt5란 Qt의 레이아웃에 파이썬 코드를 연결하여 GUI 프로그램을 가능하게 해주는 툴킷이다.
### 1. pip 설치
pip은 파이썬의 패키자 관리자이다.
설치 전에 버전을 확인하려면 cmd창에서 아래와 같이 입력한다.
```
> python -m pip --version
```
아래와 같이 나온다면 설치가 된 것이다.
```
pip 19.3.1 from C:\Users\~~~~~~\Python\Python38-32\lib\site-packages\pip (python 3.8)
```
만약 다른 메시지가 출력 되면 [여기](https://pip.pypa.io/en/stable/installing/)에서 get-pip.py 파일을 다운 받아 vscode 로 열고 실행한다.

설치가 끝나면 pip을 최신버전으로 업그레이드하기 위해 cmd 창에서 아래와 같이 실행한다.
```
> python -m pip install -U pip 
```

### 2. PyQt5 설치 

```
> python -m pip list
```
위와 같이 입력하여 pip으로 설치된 패키지들을 확인 할 수 있다.

PyQt5를 설치하기 위해 cmd창에서 아래와 같이 입력한다.
```
> python -m pip install PyQt5
```
몇 분 후 설치가 완료되는 것을 확인 할 수 있다.
* * *
Qt-Designer 설치
----------------
Qt-Designer의 설치 방법은 2가지가 있다.
### 1. ANACONDA를 이용한 설치
https://www.anaconda.com/distribution/#download-section 에서 자신의 환경에 맞는 버전을 다운로드 하면 된다. 
설치가 완료되면 시작메뉴에서 Anaconda Prompt.exe 파일을 실행한 뒤 도스창에서 "designer" 라고 입력하면 Qt-Designer가 실행된다.

### 2. pip을 이용한 설치
Qt-Designer를 설치하려면 cmd창에서 아래와 같이 입력한다.
```
> python -m pip install PyQt5-tools
```
설치가 완료되면 파이썬 설치 경로로 가서 Lib\site-packages\pyqt5_tools\Qt\bin 폴더 안에 designer.exe 파일을 실행한다.
ex)
```
C:\Users\사용자명\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\pyqt5_tools\Qt\bin
```
* * *
### 참고
- pip 설치 : https://pinocc.tistory.com/198
- 예제&학습 : [예제로 배우는 PyQt5](https://www.opentutorials.org/module/544)