# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
    QLineEdit, QListView, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1258, 853)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* \uc2a4\ud0c0\uc77c\uc740 \uc678\ubd80 style.qss \ud30c\uc77c\uc5d0\uc11c \ub85c\ub4dc\ub429\ub2c8\ub2e4. */")
        self.horizontalLayout_main = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_main.setSpacing(0)
        self.horizontalLayout_main.setObjectName(u"horizontalLayout_main")
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.centralwidget)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_1 = QPushButton(self.leftMenuFrame)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(0, 45))
        self.btn_1.setCheckable(True)
        self.btn_1.setChecked(True)

        self.verticalMenuLayout.addWidget(self.btn_1)

        self.btn_2 = QPushButton(self.leftMenuFrame)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(0, 45))
        self.btn_2.setCheckable(True)

        self.verticalMenuLayout.addWidget(self.btn_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalMenuLayout.addItem(self.verticalSpacer)

        self.btn_settings = QPushButton(self.leftMenuFrame)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 45))

        self.verticalMenuLayout.addWidget(self.btn_settings)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.horizontalLayout_main.addWidget(self.leftMenuBg)

        self.widget_center = QWidget(self.centralwidget)
        self.widget_center.setObjectName(u"widget_center")
        self.verticalLayout_center = QVBoxLayout(self.widget_center)
        self.verticalLayout_center.setObjectName(u"verticalLayout_center")
        self.verticalLayout_center.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.widget_center)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.verticalLayout_page1 = QVBoxLayout(self.page_table)
        self.verticalLayout_page1.setObjectName(u"verticalLayout_page1")
        self.tableView = QTableView(self.page_table)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_page1.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.page_table)
        self.page_list_search = QWidget()
        self.page_list_search.setObjectName(u"page_list_search")
        self.verticalLayout_page2 = QVBoxLayout(self.page_list_search)
        self.verticalLayout_page2.setObjectName(u"verticalLayout_page2")
        self.frame_search = QFrame(self.page_list_search)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_search)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_search = QLineEdit(self.frame_search)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.horizontalLayout.addWidget(self.lineEdit_search)

        self.btn_search = QPushButton(self.frame_search)
        self.btn_search.setObjectName(u"btn_search")

        self.horizontalLayout.addWidget(self.btn_search)


        self.verticalLayout_page2.addWidget(self.frame_search)

        self.listView = QListView(self.page_list_search)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_page2.addWidget(self.listView)

        self.stackedWidget.addWidget(self.page_list_search)

        self.verticalLayout_center.addWidget(self.stackedWidget)


        self.horizontalLayout_main.addWidget(self.widget_center)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"qt_django", None))
#if QT_CONFIG(tooltip)
        self.btn_1.setToolTip(QCoreApplication.translate("MainWindow", u"\ud14c\uc774\ube14 (Ctrl+1)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"\ud14c\uc774\ube14", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.btn_2.setToolTip(QCoreApplication.translate("MainWindow", u"\ub9ac\uc2a4\ud2b8 \ubc0f \uac80\uc0c9", None))
#endif // QT_CONFIG(tooltip)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
#if QT_CONFIG(tooltip)
        self.btn_settings.setToolTip(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
#endif // QT_CONFIG(tooltip)
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4\ub97c \uc785\ub825\ud558\uc138\uc694...", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
    # retranslateUi

