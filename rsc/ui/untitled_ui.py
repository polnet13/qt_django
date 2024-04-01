# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 631)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 10, 791, 571))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 761, 21))
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 40, 761, 321))
        self.tableView.setFrameShape(QFrame.Box)
        self.tableView.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 360, 401, 41))
        self.label_2.setCursor(QCursor(Qt.UpArrowCursor))
        self.label_2.setFocusPolicy(Qt.WheelFocus)
        self.label_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label_2.setWordWrap(True)
        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(380, 400, 371, 131))
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 469, 261, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_tubedown = QPushButton(self.layoutWidget)
        self.btn_tubedown.setObjectName(u"btn_tubedown")

        self.horizontalLayout_2.addWidget(self.btn_tubedown)

        self.btn_path_tube = QPushButton(self.layoutWidget)
        self.btn_path_tube.setObjectName(u"btn_path_tube")

        self.horizontalLayout_2.addWidget(self.btn_path_tube)

        self.layoutWidget1 = QWidget(self.tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 400, 261, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_subtitle_site = QPushButton(self.layoutWidget1)
        self.btn_subtitle_site.setObjectName(u"btn_subtitle_site")

        self.horizontalLayout.addWidget(self.btn_subtitle_site)

        self.btn_path_subtitle = QPushButton(self.layoutWidget1)
        self.btn_path_subtitle.setObjectName(u"btn_path_subtitle")

        self.horizontalLayout.addWidget(self.btn_path_subtitle)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 761, 131))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 10, 551, 31))
        self.btn_outpath = QPushButton(self.frame)
        self.btn_outpath.setObjectName(u"btn_outpath")
        self.btn_outpath.setGeometry(QRect(10, 10, 161, 28))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 90, 551, 31))
        self.btn_outpath_4 = QPushButton(self.frame)
        self.btn_outpath_4.setObjectName(u"btn_outpath_4")
        self.btn_outpath_4.setGeometry(QRect(10, 90, 161, 28))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 60, 551, 31))
        self.btn_outpath_3 = QPushButton(self.tab_2)
        self.btn_outpath_3.setObjectName(u"btn_outpath_3")
        self.btn_outpath_3.setGeometry(QRect(20, 60, 161, 28))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_outpath.clicked.connect(MainWindow.slot_outpath)
        self.lineEdit.returnPressed.connect(MainWindow.slot_lineEdit)
        self.btn_subtitle_site.clicked.connect(MainWindow.slot_subtitle_site)
        self.btn_path_tube.clicked.connect(MainWindow.slot_path_tube)
        self.btn_path_subtitle.clicked.connect(MainWindow.slot_path_subtitle)
        self.btn_tubedown.clicked.connect(MainWindow.slot_tubedown)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ub4dc\ub798\uadf8\uc564 \ub4dc\ub86d \ud14c\uc2a4\ud2b8 \ud654\uba74\uc73c\ub85c vtt \uc790\ub9c9 \ud30c\uc77c\ub9cc \uc778\uc2dd\ud568", None))
        self.btn_tubedown.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1 down", None))
        self.btn_path_tube.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1\ub2e4\uc6b4 \uacbd\ub85c", None))
        self.btn_subtitle_site.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub9c9 \uc0ac\uc774\ud2b8", None))
        self.btn_path_subtitle.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub9c9\ub2e4\uc6b4 \uacbd\ub85c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uc720\ud29c\ube0c \ub2e4\uc6b4\ub85c\ub4dc", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_outpath.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1 \uc800\uc7a5\uacbd\ub85c \uc124\uc815", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_outpath_4.setText(QCoreApplication.translate("MainWindow", u"\ud589 \uc0ad\uc81c \ub2e8\ucd95\ud0a4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_outpath_3.setText(QCoreApplication.translate("MainWindow", u"\uc790\ub9c9 \uc0ac\uc774\ud2b8 \uc124\uc815", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
    # retranslateUi

