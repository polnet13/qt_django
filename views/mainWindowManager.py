from PySide6.QtWidgets import QMainWindow
from rsc.ui.untitled_ui import Ui_MainWindow
# 웹 바로가기
from PySide6.QtGui import QDesktopServices 
from PySide6.QtCore import QUrl   
# 단축키 설정
from PySide6.QtGui import QKeySequence, QShortcut  

import pandas as pd
import os
from views.control import orm, tube, hangle
import time
# from views.control import hangle

 

# 머니북 ui 클래스
class mainWindow(QMainWindow, Ui_MainWindow): # Ui_MainWindow == rec.ui.MainWindow

    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        # path 설정
        self.file_paths = []
        self.base_dir = os.path.dirname(os.path.dirname(__file__))  
        self.outpath = r'C:\Users\prude\OneDrive\바탕 화면\유튜브 영상' 
        self.label.setText(self.outpath)
        # 모든 데이터 조회
        orm.reset_tableview(self.tableView)
        # 테이블 정리
        self.tableView.setColumnWidth(0, 0)  # id 안보이게
        self.tableView.setColumnWidth(1, 400)  # id 안보이게
        self.tableView.setColumnWidth(2, 200)  # id 안보이게
        self.tableView.setColumnWidth(3, 100)  # id 안보이게
        # 단축키 설정
        self.shortcut = QShortcut(QKeySequence.Delete, self)
        self.shortcut.activated.connect(self.shortcut_del)
    
    ##############
    ## 슬롯함수 ##
    ##############
    def slot_tubedown(self):
        # 다운로드 안되면 작업경로 변경해서 다운하면 됨
        pass

    def slot_outpath(self):
        # path = 경로가져 오기
        # self.outpath = path
        # self.label.setText(self.outpath)
        pass

    def slot_delete(self):
        rows = orm.get_selected_pk(self.tableView)
        orm.delete_rows(rows, self.tableView)
        
    def slot_lineEdit(self):
        url = self.lineEdit.text()
        try:
            orm.create_tube(url, self.tableView)
            tube.get_video(url, self.outpath)
            tube.getWebSubtitle(f"https://downsub.com/?url={url}")
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

