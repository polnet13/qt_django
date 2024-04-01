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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1302, 991)
        self.actionselect_file = QAction(MainWindow)
        self.actionselect_file.setObjectName(u"actionselect_file")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 40, 911, 621))
        self.videoFrame = QHBoxLayout(self.horizontalLayoutWidget)
        self.videoFrame.setObjectName(u"videoFrame")
        self.videoFrame.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.videoFrame.addItem(self.verticalSpacer)

        self.playSlider = QSlider(self.centralwidget)
        self.playSlider.setObjectName(u"playSlider")
        self.playSlider.setGeometry(QRect(50, 690, 841, 22))
        self.playSlider.setOrientation(Qt.Horizontal)
        self.playTimer = QLabel(self.centralwidget)
        self.playTimer.setObjectName(u"playTimer")
        self.playTimer.setGeometry(QRect(910, 690, 64, 15))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 720, 163, 23))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_play = QToolButton(self.widget)
        self.btn_play.setObjectName(u"btn_play")

        self.horizontalLayout.addWidget(self.btn_play)

        self.btn_pause = QToolButton(self.widget)
        self.btn_pause.setObjectName(u"btn_pause")

        self.horizontalLayout.addWidget(self.btn_pause)

        self.btn_stop = QToolButton(self.widget)
        self.btn_stop.setObjectName(u"btn_stop")

        self.horizontalLayout.addWidget(self.btn_stop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1302, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionselect_file)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionselect_file.setText(QCoreApplication.translate("MainWindow", u"select file", None))
        self.playTimer.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.btn_play.setText(QCoreApplication.translate("MainWindow", u"play", None))
        self.btn_pause.setText(QCoreApplication.translate("MainWindow", u"pause", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ube44\ub514\uc624 \uc5f4\uae30", None))
    # retranslateUi

