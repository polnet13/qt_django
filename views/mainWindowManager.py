from rsc.ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from .orm import *

class mainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

    def slot1(self):
        print('slot1 함수 실행: 이름 입력함수 연결')
        inputData('kim', 20)

        return self
