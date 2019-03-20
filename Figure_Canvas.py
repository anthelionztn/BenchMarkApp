#-*-coding:utf-8-*-

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键
#     label_x = ''
#     label_y = ''
#     chFont = fm.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
#     # def __init__(self, parent=None, width=3.6, height=2, dpi=100):
#     def __init__(self, parent=None, width=12, height=9, dpi=100):
#         # fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
#         fig = plt.figure(figsize=(width, height), dpi=80)
#         FigureCanvas.__init__(self, fig) # 初始化父类
#         self.setParent(parent)
#         # self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
#         self.axes = fig.subplots(1, 1)
#
#     def plotScatter(self, data_x, data_y, label_x, label_y, x_discrete, y_discrete, color, marker):
#
#         plt.title(label_x + "-" + label_y, fontproperties = self.chFont)
#         plt.scatter(data_x, data_y, c = color, marker = marker )
#         if x_discrete:
#             plt.xticks(data_x, data_x, rotation = 45, fontproperties = self.chFont, fontsize = 7)
#         if y_discrete:
#             plt.yticks(data_y, data_y, fontproperties = self.chFont, fontsize = 7)
#         plt.show()
#         # self.axes.scatter(data_x, data_y)
#         # self.axes.set_title(label_x + "-" + label_y + "Trend")
#   -------------------------------------------------------

class Figure_Canvas():   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键
    label_x = ''
    label_y = ''
    chFont = fm.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')
    # def __init__(self, parent=None, width=3.6, height=2, dpi=100):
    def __init__(self, parent=None, width=12, height=9, dpi=100):
        # fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        fig = plt.figure(figsize=(width, height), dpi=80)
        #FigureCanvas.__init__(self, fig) # 初始化父类
        #self.setParent(parent)
        # self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.axes = fig.subplots(1, 1)

    def plotScatter(self, data_x, data_y, label_x, label_y, x_discrete, y_discrete, color, marker):

        plt.title(label_x + " vs " + label_y, fontproperties=self.chFont)
        plt.scatter(data_x, data_y, c=color, marker=marker)
        if x_discrete:
            plt.xticks(data_x, data_x, rotation=45, fontproperties=self.chFont, fontsize=7)
        if y_discrete:
            plt.yticks(data_y, data_y, fontproperties=self.chFont, fontsize=7)
        plt.show()
        # self.axes.scatter(data_x, data_y)
        # self.axes.set_title(label_x + "-" + label_y + "Trend")