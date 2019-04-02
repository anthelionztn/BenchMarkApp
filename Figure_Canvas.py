# -*-coding:utf-8-*-

import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import numpy as np

class Figure_Canvas():
    label_x = ''
    label_y = ''
    if platform.system() == "Windows":
        chFont = fm.FontProperties(fname=r'C:\WINDOWS\Fonts\MSYH.TTC')  # Windows系统字体地址
        fontSize = 10
    else:
        chFont = fm.FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc')  # Mac OS系统字体地址
        fontSize = 7

    def __init__(self, parent=None, width=12, height=9, dpi=100):
        fig = plt.figure(figsize=(width, height), dpi=80)
        self.axes = fig.subplots(1, 1)

    def plotScatter(self, data_x, data_y, datalabel, datalabelSelected, label_x, label_y, x_discrete, y_discrete, color,
                    marker):

        plt.title(label_x + " vs " + label_y, fontproperties=self.chFont)
        plt.scatter(data_x, data_y, c=color, marker=marker)
        if datalabelSelected:
            for x, y, z in zip(data_x, data_y, datalabel):
                plt.text(x, y + 500, z, ha='center', va='bottom', fontproperties=self.chFont, fontsize=self.fontSize)
        if x_discrete:  # 如果横轴离散化选中
            plt.xticks(data_x, data_x, rotation=45, fontproperties=self.chFont, fontsize=self.fontSize)
        if y_discrete:  # 如果纵轴离散化选中
            plt.yticks(data_y, data_y, fontproperties=self.chFont, fontsize=self.fontSize)
        plt.xlabel(label_x, fontproperties=self.chFont)
        plt.ylabel(label_y, fontproperties=self.chFont)
        plt.show()

    def plotScatterFit(self, data_x, data_y, datalabel, datalabelSelected, label_x, label_y, color, marker, source_x,
                       source_y, degree):

        plt.title(label_x + " vs " + label_y, fontproperties=self.chFont)
        plt.scatter(data_x, data_y, c=color, marker=marker)
        if datalabelSelected:
            for x, y, z in zip(data_x, data_y, datalabel):
                plt.text(x, y + 500, z, ha='center', va='bottom', fontproperties=self.chFont, fontsize=self.fontSize)
        self.fit(source_x, source_y, degree)
        plt.xlabel(label_x, fontproperties=self.chFont)
        plt.ylabel(label_y, fontproperties=self.chFont)
        plt.xlim((min(data_x) * 0.8, max(data_x) * 1.2))
        plt.ylim((min(data_y) * 0.8, max(data_y) * 1.2))
        plt.show()

    def fit(self, source_x, source_y, degree):  # 根据所选自由度拟合多项式
        z = np.polyfit(source_x, source_y, degree)
        p = np.poly1d(z)  # 生成多项式对象
        plt.plot(sorted(source_x), p(sorted(source_x)), linestyle=':')
