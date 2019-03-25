# -*- coding: utf-8 -*-

# 该文件用于继承PyUIC生成的Ui_MainWindow类，并编写控制逻辑

from pandasModel import *
from mainWindowUI import *
from Figure_Canvas import *
# from PyQt5.Qt import QRegExpValidator
# from PyQt5.Qt import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    dataset = pd.DataFrame()    #以dataframe的形式存储数据源选择的文件数据
    result_reindex = pd.DataFrame()  #以dataframe的形式存储tabView中的数据
    catelist = pd.DataFrame()   #以dateframe的形式存储字段分组信息
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #设置lineEdit数据验证
        regInt = '^0$|^[1-9]\d*$'  # 不接受09这样的为整数
        regFloat = '^0\.\d+$|^[1-9]\d*\.\d+$'   # 接受0.00、0.360这样的为小数，不接受00.36，思路:若整数位为零,小数位可为任意整数，但小数位数至少为1位，若整数位为自然数打头，后面可添加任意多个整数，小数位至少1位
        regx = QRegExp(regInt+'|'+regFloat)
        validator = QRegExpValidator(regx)
        self.lineEditX.setValidator(validator)
        self.lineEditY.setValidator(validator)

        #编写各信号槽
        self.listWidget_carSelected.setContextMenuPolicy(3)
        self.listWidget_carSelected.itemDoubleClicked.connect(self.delCarfromList)   #双击删除车型
        self.listWidget_paraSelected.itemDoubleClicked.connect(self.delParafromList)    #双击删除参数
        self.listWidget_carSelect.itemDoubleClicked.connect(self.addCartoList) #双击加入已选车型列表
        self.listWidget_paraList.itemDoubleClicked.connect(self.addParatoList)  #双击加入已选参数列表
        self.pushButton_carClear.clicked.connect(self.clearAllCarItems) #单击清除全部车型
        self.pushButton_paraClear.clicked.connect(self.clearAllParaItems)   #单击清除全部参数
        self.pushButton_carAllSelect.clicked.connect(self.addAllCartoList)  #单击加入全部车型
        self.pushButton_paraAllSelect.clicked.connect(self.addAllParatoList)    #单击加入全部参数
        self.pushButton_dataSource.clicked.connect(self.openFile)   #单击选择数据源
        self.pushButton_query.clicked.connect(self.quaryData)   #单击查询按钮切换tab，并显示查询结果
        self.pushButton_back.clicked.connect(self.tabToggle)    #切换tab
        self.comboBox_cate.currentTextChanged.connect(self.cateSel)

        self.pushButton_plot.clicked.connect(self.draw) #单击绘制按钮画图
        self.pushButton_insert.clicked.connect(self.insert)  #单击插入按钮插入新点
        self.comboBox_paraH.currentTextChanged.connect(self.disableLineEdit)
        self.comboBox_paraV.currentTextChanged.connect(self.disableLineEdit)



    def openFile(self): #选择数据源文件，并将文件中数据写入车型列表中
        try:
            fileName = QtWidgets.QFileDialog.getOpenFileName(self,'选择数据源文件','.')
        except FileNotFoundError:
            return
        if fileName[0]!='':
            data = self.getData(fileName[0])
            self.listWidget_carSelect.addItems(data[0])
            self.listWidget_paraList.addItems(data[1][1:])
            self.comboBox_cate.addItems(self.catelist['字段分组'])
        else:
            return

    def addCartoList(self, item):   #判断车型列表中被双击的item是否已经存在已选车型列表中，如果不存在则将其加入
        for i in range(self.listWidget_carSelected.count()):
            if item.text()==self.listWidget_carSelected.item(i).text():
                return
        self.listWidget_carSelected.addItem(item.text())


    def addAllCartoList(self):  #全选车辆，并将其全部加入左边已选车辆列表中
        self.clearAllCarItems()
        self.listWidget_carSelected.addItems(self.dataset.iloc[:,0].values)


    def delCarfromList(self, item):  #删除已选车辆列表中的某一条数据
        self.listWidget_carSelected.removeItemWidget(self.listWidget_carSelected.takeItem(self.listWidget_carSelected.row(item)))


    def clearAllCarItems(self): #清空全部已选车辆
        self.listWidget_carSelected.clear()


    def getData(self, adr):
        self.dataset = pd.read_excel(adr, sheet_name=0)
        self.catelist = pd.read_excel(adr, sheet_name=1)
        carList = self.dataset.iloc[:,0].values
        paraList = self.dataset.columns.values.tolist()
        return (carList, paraList)


    def addParatoList(self, item):   # 判断参数列表中被双击的item是否已经存在已选参数列表中，如果不存在则将其加入
        for i in range(self.listWidget_paraSelected.count()):
            if item.text() == self.listWidget_paraSelected.item(i).text():
                return
        self.listWidget_paraSelected.addItem(item.text())


    def addAllParatoList(self):  # 全选当前参数列表中的参数，并将其全部加入左边已选参数列表中
        self.clearAllParaItems()
        #self.listWidget_paraSelected.addItems(self.dataset.columns.values.tolist())
        for i in range(self.listWidget_paraList.count()):
            self.listWidget_paraSelected.addItem(self.listWidget_paraList.item(i).text())

    def delParafromList(self, item):  # 删除已选参数列表中的某一条数据
        self.listWidget_paraSelected.removeItemWidget(self.listWidget_paraSelected.takeItem(self.listWidget_paraSelected.row(item)))

    def clearAllParaItems(self):  # 清空全部已选参数
        self.listWidget_paraSelected.clear()

    def quaryData(self):
        if self.listWidget_carSelected.count() == 0:
            QtWidgets.QMessageBox.warning(self, '警告', '未选择对比车型')
        elif self.listWidget_paraSelected.count() == 0:
            QtWidgets.QMessageBox.warning(self, '警告', '未选择对比参数')
        else:
            carList = self.itemToList(self.listWidget_carSelected)
            paraList = self.itemToList(self.listWidget_paraSelected)
            result = pd.DataFrame()
            if '车型' not in paraList:
                paraList.insert(0, '车型')
            for i in carList:
                result = pd.concat([result, self.dataset.loc[self.dataset['车型'] == i, paraList]])
            self.result_reindex = result.reset_index(drop=True)
            self.tabToggle()
            self.dataToTab(self.result_reindex)
            self.comboBox_paraH.clear()
            self.comboBox_paraV.clear()
            self.comboBox_paraH.addItems(paraList[:])  #将已选参数加入可视化界面的下拉菜单
            self.comboBox_paraV.addItems(paraList[:])  #将已选参数加入可视化界面的下拉菜单

    def itemToList(self, listwidget):
        lst = []
        for i in range(listwidget.count()):
            lst.append(listwidget.item(i).text())
        return lst

    def tabToggle(self):
        if self.tabWidget.currentIndex() == 0:
            self.tabWidget.setCurrentIndex(1)
        else:
            self.tabWidget.setCurrentIndex(0)

    def dataToTab(self, df):
        model = PandasModel(df)
        self.tableView.setModel(model)

    def draw(self):
        if self.comboBox_paraH.currentText()!='' and self.comboBox_paraV.currentText()!='':
            plt.close()
            label_x = self.comboBox_paraH.currentText()
            label_y = self.comboBox_paraV.currentText()

            x = self.result_reindex[label_x]
            y = self.result_reindex[label_y]

            dr = Figure_Canvas()
            dr.plotScatter(x, y,
                            label_x, label_y,
                            self.checkBox_paraHdiscr.isChecked(), self.checkBox_paraVdiscr.isChecked(),
                            'b', 'o')
        else:
            QtWidgets.QMessageBox.warning(self, '警告', '请先进行查询操作')

    def insert(self):
        if self.comboBox_paraH.currentText() != '' and self.comboBox_paraV.currentText() != '':
            plt.close()
            label_x = self.comboBox_paraH.currentText()
            label_y = self.comboBox_paraV.currentText()
            colorDict = {'蓝色':'b',
                         '绿色':'g',
                         '红色':'r',
                         '青色':'c',
                         '洋红色':'m',
                         '黄色':'y',
                         '黑色':'k'}
            newColor = colorDict[self.comboBox_pointColor.currentText()]
            x = self.result_reindex[label_x]
            y = self.result_reindex[label_y]

            dr = Figure_Canvas()

            if self.lineEditX.text() == '' or self.lineEditY.text() == '':
                QtWidgets.QMessageBox.warning(self, '警告', '请先输入插入点坐标')
            else:
                newPointX = x.append(pd.Series(float(self.lineEditX.text())))
                newPointY = y.append(pd.Series(float(self.lineEditY.text())))
                color = ['b'] * (len(x))
                color.append(newColor)

                dr.plotScatter(newPointX, newPointY,
                           label_x, label_y,
                           self.checkBox_paraHdiscr.isChecked(), self.checkBox_paraVdiscr.isChecked(),
                           color, 'o')

        else:
            QtWidgets.QMessageBox.warning(self, '警告', '请先进行查询操作')

    def cateSel(self):  #获取选中分类的字段起始索引，并按索引显示相应字段
        self.listWidget_paraList.clear()
        curr = self.comboBox_cate.currentText()
        begin = pd.Series.tolist(self.catelist.loc[self.catelist['字段分组']==curr,'字段开始'])  #获取字段开始的列索引
        end = pd.Series.tolist(self.catelist.loc[self.catelist['字段分组']==curr,'字段结束'])    #获取字段结束的列索引
        paraList = self.dataset.columns.values.tolist()
        self.listWidget_paraList.addItems(paraList[begin[0]:end[0]+1:1])

    def disableLineEdit(self):  #根据所选横纵坐标的数据类型，判断插入点是否可编辑
        if self.comboBox_paraH.currentText() != '' and self.comboBox_paraV.currentText()!='':   #确认横纵坐标下拉菜单有值
            label_x = self.comboBox_paraH.currentText()
            label_y = self.comboBox_paraV.currentText()
            x = self.result_reindex[label_x]    #获取横坐标数据
            y = self.result_reindex[label_y]    #获取纵坐标数据
            if x.dtype=='object' or y.dtype=='object':  #判断横纵坐标的数据类型是否为数值型
                self.lineEditX.setEnabled(False)
                self.lineEditY.setEnabled(False)
            else:
                self.lineEditX.setEnabled(True)
                self.lineEditY.setEnabled(True)