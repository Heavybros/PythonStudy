import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

# UI 파일 연결
# 단 UI 파일은 파이썬 코드 파일과 같은 디렉토리에 위치해야 한다.

# form_class = uic.loadUiType('D:/PythonExam/UsingPyQ5/uiTest.ui')[0]

# # 화면을 띄우는데 사용되는 class 선언
# class WindowClass(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

# if __name__ == "__main__":
#     # QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)

#     # WindowClass의 인스턴스 생성
#     myWindow = WindowClass()

#     # 프로그램 화면을 보여주는 코드
#     myWindow.show()

#     # 프로그램 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()

class Form(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi('D:/PythonExam/UsingPyQ5/uiTest.ui')
        self.ui.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())