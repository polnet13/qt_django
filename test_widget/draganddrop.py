import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_paths = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Drag and Drop")
        self.setGeometry(100, 100, 300, 300)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.file_paths.append(url.toLocalFile())
        print(self.file_paths)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())