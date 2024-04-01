from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QTabWidget instance
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create tabs
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        # Add tabs to the QTabWidget instance
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        # Add widgets to the first tab
        self.layout1 = QVBoxLayout()
        self.label1 = QLabel("This is a label")
        self.line_edit1 = QLineEdit()
        self.layout1.addWidget(self.label1)
        self.layout1.addWidget(self.line_edit1)
        self.tab1.setLayout(self.layout1)

        # Add widgets to the second tab
        self.layout2 = QVBoxLayout()
        self.label2 = QLabel("This is another label")
        self.line_edit2 = QLineEdit()
        self.layout2.addWidget(self.label2)
        self.layout2.addWidget(self.line_edit2)
        self.tab2.setLayout(self.layout2)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
