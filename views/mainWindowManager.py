from PySide6.QtWidgets import QMainWindow
from rsc.ui.untitled_ui import Ui_MainWindow
# 웹 바로가기
from PySide6.QtGui import QDesktopServices 
from PySide6.QtCore import QUrl   
# 단축키 설정
from PySide6.QtGui import QKeySequence, QShortcut  

import pandas as pd
import os
from views.control import orm 
import time
# from views.control import hangle

 

# 머니북 ui 클래스
class mainWindow(QMainWindow, Ui_MainWindow): # Ui_MainWindow == rec.ui.MainWindow

    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

        # 시그널과 슬롯 연결
        self.btn_1.clicked.connect(self.slot_btn1)
        self.btn_2.clicked.connect(self.slot_btn2)
    
    ##############
    ## 슬롯함수 ##
    ##############
    def slot_btn1(self):
        self.stackedWidget.setCurrentIndex(0)

    def slot_btn2(self):
        self.stackedWidget.setCurrentIndex(1)



    def slot_delete(self):
        rows = orm.get_selected_pk(self.tableView)
        orm.delete_rows(rows, self.tableView)
        
    def slot_lineEdit(self):
        url = self.lineEdit.text()
        try:
            orm.create_tube(url, self.tableView)
        except Exception as e:
            self.statusbar.showMessage(str(e)[:50], timeout=3000)
        

    def slot_subtitle_site(self, url):
        QDesktopServices.openUrl(QUrl(f"https://downsub.com/?url={url}"))
    
    def slot_path_tube(self):
        path = self.outpath
        QDesktopServices.openUrl(QUrl.fromLocalFile(path))
    
    def slot_path_subtitle(self):
        path = r'C:\Users\prude\Downloads'
        QDesktopServices.openUrl(QUrl.fromLocalFile(path))
        
    ##################################################################    
    # 드래그앤 드랍 
    ##################################################################
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            for url in event.mimeData().urls():
                self.file_paths.append(str(url.toLocalFile()))
            subtitle_files = [f for f in self.file_paths if f.endswith('.vtt') or f.endswith('.srt')]
            self.listWidget.addItems(subtitle_files)
        else:
            event.ignore()
    ##################################################################    
    # 단축키 함수
    ##################################################################   
    def shortcut_del(self):
        self.slot_delete()
    ##############
    ## 도구모음 ##
    ##############
    # def on_click(self, index):
    #     print(f"Selected cell: {index.row()}, {index.column()}")
    #     value = input("Enter new value: ")
    #     self.model.setData(index, value)
    #     print(f"New value: {value}")
        
    # def on_cell_changed(self):
    #     print('on_cell_changed')
    #     pass


    ###############
    ## 커스텀함수 ##
    ###############

