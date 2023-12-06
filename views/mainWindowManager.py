from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
 
from rsc.ui_ui import Ui_MainWindow

import pandas as pd
from views import orm




class mainWindow(QMainWindow, Ui_MainWindow): # Ui_MainWindow == rec.ui.MainWindow

    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        # db 데이터 보여주기
        self._queryset = orm.all()
        self._df = None
        self._qmodel = None    
        self.queryset_to_df()
        self.df_to_qmodel()
        self.tableView.setModel(self._qmodel) 

    ##############
    ## 슬롯함수 ##
    ##############
    def slot1(self):
        name = self.plainTextEdit_1.toPlainText()
        self.plainTextEdit_1.clear()
        age = self.plainTextEdit_2.toPlainText()
        self.plainTextEdit_2.clear()
        if name=='' or age=='':
            print('빈값은 저장 할 수 없어요')
        else:
            orm.inputData(name, age)
        self.getAll()
    
    def getAll(self):
        self._queryset = orm.all()  
        self.queryset_to_df() 
        self.df_to_qmodel() 
        self.tableView.setModel(self._qmodel)  

    def clearTable(self):
        orm.delete_all()
        self.getAll() 

    ##############
    ## 도구모음 ##
    ##############
    def queryset_to_df(self):
        """
        장고 queryset을 Pandas DataFrame으로 변환 
        Args:
            queryset: 장고 쿼리셋
        Returns:
            판다스 데이터프레임
        """
        if self._queryset:
            dataframe = pd.DataFrame(self._queryset.values())
            dataframe.columns = [field.name for field in self._queryset.model._meta.fields]
            self._df = dataframe
        else:
            self._df = None
            self._qmodel = QStandardItemModel()
        return self

    def df_to_qmodel(self):
        '''
        df을 인자로 받고 QStandardItemModel 객체로 반환함
        '''
        if self._df is not None:
            model = QStandardItemModel()
            # 컬럼 헤더 생성
            model.setHorizontalHeaderLabels(self._df.columns)
            # 데이터를 모델로 치환
            for row in range(self._df.shape[0]):
                for column in range(self._df.shape[1]):
                    item = QStandardItem(str(self._df.iloc[row, column]))
                    model.setItem(row, column, item)
            self._qmodel = model
        

