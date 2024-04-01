import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QShortcut
from PySide6.QtCore import QTimer
 

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 마우스 좌표 값을 표시할 레이블 생성
        self.label = QLabel()
        # 레이블을 윈도우에 배치
        self.label.setGeometry(101, 110, 200, 50) # 위치와 크기 지
        self.label.setAlignment(Qt.AlignCenter)
        self.label.show()
       
        
        # 마우스 좌표 값을 업데이트하는 함수
        def update_mouse_position():
            x, y = QCursor.pos().x(), QCursor.pos().y()
            self.label.setText(f"x: {x}, y: {y}")

        # 100ms마다 마우스 좌표 값을 업데이트
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(update_mouse_position)
 
        # QTimer: 시간이 종료되면 timeout 시그널을 발생시킴 (계속 반복함)
        self.timer.start()
        
        # q 버튼에 대한 단축키 설정
        shortcut = QShortcut(Qt.Key_Q, self)
        shortcut.activated.connect(self.on_shortcut)

    def on_shortcut(self):
        # q 버튼이 입력되면 QTimer를 종료하고 메인창에 좌표를 표시
        self.timer.stop()
        self.label.setText(f"x: {QCursor.pos().x()}, y: {QCursor.pos().y()}")


if __name__ == '__main__':
    print('실행')
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("마우스 좌표 표시1")
    window.show()
    sys.exit(app.exec())
 
 