# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 660)
        MainWindow.setMinimumSize(QtCore.QSize(800, 660))
        MainWindow.setMaximumSize(QtCore.QSize(800, 660))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_query = QtWidgets.QWidget()
        self.tab_query.setObjectName("tab_query")
        self.listWidget_carSelected = QtWidgets.QListWidget(self.tab_query)
        self.listWidget_carSelected.setGeometry(QtCore.QRect(20, 70, 351, 192))
        self.listWidget_carSelected.setObjectName("listWidget_carSelected")
        self.label_carSelected = QtWidgets.QLabel(self.tab_query)
        self.label_carSelected.setGeometry(QtCore.QRect(20, 40, 104, 26))
        self.label_carSelected.setObjectName("label_carSelected")
        self.label_carSelect = QtWidgets.QLabel(self.tab_query)
        self.label_carSelect.setGeometry(QtCore.QRect(20, 10, 101, 26))
        self.label_carSelect.setObjectName("label_carSelect")
        self.listWidget_carSelect = QtWidgets.QListWidget(self.tab_query)
        self.listWidget_carSelect.setGeometry(QtCore.QRect(400, 70, 351, 192))
        self.listWidget_carSelect.setObjectName("listWidget_carSelect")
        self.label_paraSelect = QtWidgets.QLabel(self.tab_query)
        self.label_paraSelect.setGeometry(QtCore.QRect(20, 300, 101, 26))
        self.label_paraSelect.setObjectName("label_paraSelect")
        self.label_paraSelected = QtWidgets.QLabel(self.tab_query)
        self.label_paraSelected.setGeometry(QtCore.QRect(20, 330, 104, 26))
        self.label_paraSelected.setObjectName("label_paraSelected")
        self.listWidget_paraSelected = QtWidgets.QListWidget(self.tab_query)
        self.listWidget_paraSelected.setGeometry(QtCore.QRect(20, 360, 351, 192))
        self.listWidget_paraSelected.setObjectName("listWidget_paraSelected")
        self.pushButton_paraClear = QtWidgets.QPushButton(self.tab_query)
        self.pushButton_paraClear.setGeometry(QtCore.QRect(290, 330, 80, 26))
        self.pushButton_paraClear.setObjectName("pushButton_paraClear")
        self.pushButton_query = QtWidgets.QPushButton(self.tab_query)
        self.pushButton_query.setGeometry(QtCore.QRect(670, 559, 80, 26))
        self.pushButton_query.setAutoFillBackground(False)
        self.pushButton_query.setObjectName("pushButton_query")
        self.line_car = QtWidgets.QFrame(self.tab_query)
        self.line_car.setGeometry(QtCore.QRect(20, 30, 731, 16))
        self.line_car.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_car.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_car.setObjectName("line_car")
        self.line_para = QtWidgets.QFrame(self.tab_query)
        self.line_para.setGeometry(QtCore.QRect(20, 320, 731, 16))
        self.line_para.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_para.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_para.setObjectName("line_para")
        self.label_carList = QtWidgets.QLabel(self.tab_query)
        self.label_carList.setGeometry(QtCore.QRect(400, 40, 104, 26))
        self.label_carList.setObjectName("label_carList")
        self.label_paraList = QtWidgets.QLabel(self.tab_query)
        self.label_paraList.setGeometry(QtCore.QRect(400, 330, 104, 26))
        self.label_paraList.setObjectName("label_paraList")
        self.pushButton_carClear = QtWidgets.QPushButton(self.tab_query)
        self.pushButton_carClear.setGeometry(QtCore.QRect(290, 40, 80, 26))
        self.pushButton_carClear.setObjectName("pushButton_carClear")
        self.pushButton_paraAllSelect = QtWidgets.QPushButton(self.tab_query)
        self.pushButton_paraAllSelect.setGeometry(QtCore.QRect(670, 330, 80, 26))
        self.pushButton_paraAllSelect.setObjectName("pushButton_paraAllSelect")
        self.pushButton_carAllSelect = QtWidgets.QPushButton(self.tab_query)
        self.pushButton_carAllSelect.setGeometry(QtCore.QRect(670, 40, 80, 26))
        self.pushButton_carAllSelect.setObjectName("pushButton_carAllSelect")
        self.pushButton_dataSource = QtWidgets.QPushButton(self.tab_query)
        self.pushButton_dataSource.setGeometry(QtCore.QRect(670, 10, 80, 26))
        self.pushButton_dataSource.setObjectName("pushButton_dataSource")
        self.listWidget_paraList = QtWidgets.QListWidget(self.tab_query)
        self.listWidget_paraList.setGeometry(QtCore.QRect(400, 360, 351, 192))
        self.listWidget_paraList.setObjectName("listWidget_paraList")
        self.comboBox_cate = QtWidgets.QComboBox(self.tab_query)
        self.comboBox_cate.setGeometry(QtCore.QRect(470, 560, 191, 26))
        self.comboBox_cate.setObjectName("comboBox_cate")
        self.label_cate = QtWidgets.QLabel(self.tab_query)
        self.label_cate.setGeometry(QtCore.QRect(400, 560, 104, 26))
        self.label_cate.setObjectName("label_cate")
        self.tabWidget.addTab(self.tab_query, "")
        self.tab_visualization = QtWidgets.QWidget()
        self.tab_visualization.setObjectName("tab_visualization")
        self.tableView = QtWidgets.QTableView(self.tab_visualization)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 731, 361))
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.pushButton_back = QtWidgets.QPushButton(self.tab_visualization)
        self.pushButton_back.setGeometry(QtCore.QRect(590, 10, 80, 26))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_export = QtWidgets.QPushButton(self.tab_visualization)
        self.pushButton_export.setGeometry(QtCore.QRect(670, 10, 80, 26))
        self.pushButton_export.setObjectName("pushButton_export")
        self.line_visualization = QtWidgets.QFrame(self.tab_visualization)
        self.line_visualization.setGeometry(QtCore.QRect(10, 410, 751, 16))
        self.line_visualization.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_visualization.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_visualization.setObjectName("line_visualization")
        self.label_result = QtWidgets.QLabel(self.tab_visualization)
        self.label_result.setGeometry(QtCore.QRect(20, 10, 101, 26))
        self.label_result.setObjectName("label_result")
        self.label_graphic = QtWidgets.QLabel(self.tab_visualization)
        self.label_graphic.setGeometry(QtCore.QRect(20, 420, 101, 26))
        self.label_graphic.setObjectName("label_graphic")
        self.label_paraH = QtWidgets.QLabel(self.tab_visualization)
        self.label_paraH.setGeometry(QtCore.QRect(20, 450, 101, 26))
        self.label_paraH.setObjectName("label_paraH")
        self.label_paraV = QtWidgets.QLabel(self.tab_visualization)
        self.label_paraV.setGeometry(QtCore.QRect(20, 480, 101, 26))
        self.label_paraV.setObjectName("label_paraV")
        self.comboBox_paraH = QtWidgets.QComboBox(self.tab_visualization)
        self.comboBox_paraH.setGeometry(QtCore.QRect(100, 450, 261, 26))
        self.comboBox_paraH.setObjectName("comboBox_paraH")
        self.comboBox_paraV = QtWidgets.QComboBox(self.tab_visualization)
        self.comboBox_paraV.setGeometry(QtCore.QRect(100, 480, 261, 26))
        self.comboBox_paraV.setObjectName("comboBox_paraV")
        self.pushButton_plot = QtWidgets.QPushButton(self.tab_visualization)
        self.pushButton_plot.setGeometry(QtCore.QRect(280, 550, 80, 26))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.label_insertNewPoint = QtWidgets.QLabel(self.tab_visualization)
        self.label_insertNewPoint.setGeometry(QtCore.QRect(410, 420, 101, 26))
        self.label_insertNewPoint.setObjectName("label_insertNewPoint")
        self.label_pointX = QtWidgets.QLabel(self.tab_visualization)
        self.label_pointX.setGeometry(QtCore.QRect(410, 450, 101, 26))
        self.label_pointX.setObjectName("label_pointX")
        self.label_pointY = QtWidgets.QLabel(self.tab_visualization)
        self.label_pointY.setGeometry(QtCore.QRect(410, 480, 101, 26))
        self.label_pointY.setObjectName("label_pointY")
        self.lineEditX = QtWidgets.QLineEdit(self.tab_visualization)
        self.lineEditX.setGeometry(QtCore.QRect(495, 450, 261, 21))
        self.lineEditX.setObjectName("lineEditX")
        self.lineEditY = QtWidgets.QLineEdit(self.tab_visualization)
        self.lineEditY.setGeometry(QtCore.QRect(495, 480, 261, 21))
        self.lineEditY.setObjectName("lineEditY")
        self.pushButton_insert = QtWidgets.QPushButton(self.tab_visualization)
        self.pushButton_insert.setGeometry(QtCore.QRect(670, 550, 80, 26))
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.checkBox_paraHdiscr = QtWidgets.QCheckBox(self.tab_visualization)
        self.checkBox_paraHdiscr.setGeometry(QtCore.QRect(100, 520, 120, 26))
        self.checkBox_paraHdiscr.setObjectName("checkBox_paraHdiscr")
        self.checkBox_paraVdiscr = QtWidgets.QCheckBox(self.tab_visualization)
        self.checkBox_paraVdiscr.setGeometry(QtCore.QRect(240, 520, 120, 26))
        self.checkBox_paraVdiscr.setObjectName("checkBox_paraVdiscr")
        self.label_pointColor = QtWidgets.QLabel(self.tab_visualization)
        self.label_pointColor.setGeometry(QtCore.QRect(410, 510, 101, 26))
        self.label_pointColor.setObjectName("label_pointColor")
        self.comboBox_pointColor = QtWidgets.QComboBox(self.tab_visualization)
        self.comboBox_pointColor.setGeometry(QtCore.QRect(495, 510, 261, 26))
        self.comboBox_pointColor.setObjectName("comboBox_pointColor")
        self.comboBox_pointColor.addItem("")
        self.comboBox_pointColor.addItem("")
        self.comboBox_pointColor.addItem("")
        self.comboBox_pointColor.addItem("")
        self.comboBox_pointColor.addItem("")
        self.comboBox_pointColor.addItem("")
        self.comboBox_pointColor.addItem("")
        self.line = QtWidgets.QFrame(self.tab_visualization)
        self.line.setGeometry(QtCore.QRect(380, 430, 20, 151))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_fit = QtWidgets.QLabel(self.tab_visualization)
        self.label_fit.setGeometry(QtCore.QRect(20, 550, 101, 26))
        self.label_fit.setObjectName("label_fit")
        self.comboBox_fit = QtWidgets.QComboBox(self.tab_visualization)
        self.comboBox_fit.setGeometry(QtCore.QRect(100, 550, 171, 26))
        self.comboBox_fit.setObjectName("comboBox_fit")
        self.comboBox_fit.addItem("")
        self.comboBox_fit.addItem("")
        self.comboBox_fit.addItem("")
        self.comboBox_fit.addItem("")
        self.comboBox_fit.addItem("")
        self.comboBox_fit.addItem("")
        self.tabWidget.addTab(self.tab_visualization, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionitem1 = QtWidgets.QAction(MainWindow)
        self.actionitem1.setObjectName("actionitem1")
        self.actionb = QtWidgets.QAction(MainWindow)
        self.actionb.setObjectName("actionb")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "座椅竞品对标系统"))
        self.label_carSelected.setText(_translate("MainWindow", "已加入对比车型："))
        self.label_carSelect.setText(_translate("MainWindow", "选择车型："))
        self.label_paraSelect.setText(_translate("MainWindow", "选择参数："))
        self.label_paraSelected.setText(_translate("MainWindow", "已加入对比参数："))
        self.pushButton_paraClear.setText(_translate("MainWindow", "清空"))
        self.pushButton_query.setText(_translate("MainWindow", "查询"))
        self.label_carList.setText(_translate("MainWindow", "车型列表："))
        self.label_paraList.setText(_translate("MainWindow", "参数列表："))
        self.pushButton_carClear.setText(_translate("MainWindow", "清空"))
        self.pushButton_paraAllSelect.setText(_translate("MainWindow", "全选"))
        self.pushButton_carAllSelect.setText(_translate("MainWindow", "全选"))
        self.pushButton_dataSource.setText(_translate("MainWindow", "数据源"))
        self.label_cate.setText(_translate("MainWindow", "参数类别："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_query), _translate("MainWindow", " 数据查询"))
        self.pushButton_back.setText(_translate("MainWindow", "返回查询"))
        self.pushButton_export.setText(_translate("MainWindow", "导出"))
        self.label_result.setText(_translate("MainWindow", "对标结果："))
        self.label_graphic.setText(_translate("MainWindow", "散点图绘制："))
        self.label_paraH.setText(_translate("MainWindow", "横轴参数："))
        self.label_paraV.setText(_translate("MainWindow", "纵轴参数："))
        self.pushButton_plot.setText(_translate("MainWindow", "绘图"))
        self.label_insertNewPoint.setText(_translate("MainWindow", "插入新数据："))
        self.label_pointX.setText(_translate("MainWindow", "横轴坐标值："))
        self.label_pointY.setText(_translate("MainWindow", "纵轴坐标值："))
        self.lineEditX.setPlaceholderText(_translate("MainWindow", "请输入数值型数据"))
        self.lineEditY.setPlaceholderText(_translate("MainWindow", "请输入数值型数据"))
        self.pushButton_insert.setText(_translate("MainWindow", "插入"))
        self.checkBox_paraHdiscr.setText(_translate("MainWindow", "横轴刻度离散化"))
        self.checkBox_paraVdiscr.setText(_translate("MainWindow", "纵轴刻度离散化"))
        self.label_pointColor.setText(_translate("MainWindow", "插入点颜色："))
        self.comboBox_pointColor.setItemText(0, _translate("MainWindow", "绿色"))
        self.comboBox_pointColor.setItemText(1, _translate("MainWindow", "红色"))
        self.comboBox_pointColor.setItemText(2, _translate("MainWindow", "青色"))
        self.comboBox_pointColor.setItemText(3, _translate("MainWindow", "洋红色"))
        self.comboBox_pointColor.setItemText(4, _translate("MainWindow", "黄色"))
        self.comboBox_pointColor.setItemText(5, _translate("MainWindow", "黑色"))
        self.comboBox_pointColor.setItemText(6, _translate("MainWindow", "蓝色"))
        self.label_fit.setText(_translate("MainWindow", "拟合自由度："))
        self.comboBox_fit.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_fit.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_fit.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_fit.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_fit.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_fit.setItemText(5, _translate("MainWindow", "6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_visualization), _translate("MainWindow", "可视化"))
        self.actionitem1.setText(_translate("MainWindow", "文件"))
        self.actionb.setText(_translate("MainWindow", "b"))

