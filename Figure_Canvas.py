#-*-coding:utf-8-*-

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

class Figure_Canvas():   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键
    label_x = ''
    label_y = ''
    if platform.system()=="Windows":
        chFont = fm.FontProperties(fname=r'C:\WINDOWS\Fonts\MSYH.TTC')  # Windows系统字体地址
        fontSize = 10
    else:
        chFont = fm.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc') # Mac OS系统字体地址
        fontSize = 7

    def __init__(self, parent=None, width=12, height=9, dpi=100):
        fig = plt.figure(figsize=(width, height), dpi=80)
        self.axes = fig.subplots(1, 1)

    def plotScatter(self, data_x, data_y, label_x, label_y, x_discrete, y_discrete, color, marker):

        plt.title(label_x + " vs " + label_y, fontproperties=self.chFont)
        plt.scatter(data_x, data_y, c=color, marker=marker)
        if x_discrete:
            plt.xticks(data_x, data_x, rotation=45, fontproperties=self.chFont, fontsize=7)
        if y_discrete:
            plt.yticks(data_y, data_y, fontproperties=self.chFont, fontsize=7)
        plt.show()