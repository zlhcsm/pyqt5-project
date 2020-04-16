# -*- coding: utf-8 -*-

# @Time  : 2020-04-13 17:14

# @Author : 张磊

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# @Project : pyqt5

# @FileName: test.py.py

# @Software: PyCharm

# @  Blog:https://blog.csdn.net/zzzzlei123123123
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
import qtawesome as qta
import action as ac

import sys


class RadioButton(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setUI()

    def onClick0(self):
        self.g0Edit.setText(ac.get_message())

    def onClick50(self):
        self.g50Edit.setText(ac.get_message())

    def onClick100(self):
        self.g100Edit.setText(ac.get_message())

    def onClick150(self):
        self.g150Edit.setText(ac.get_message())

    def onClick200(self):
        self.g200Edit.setText(ac.get_message())

    def onClick250(self):
        self.g250Edit.setText(ac.get_message())



    def setUI(self):
        fa5_icon = qta.icon('fa5.flag')
        # 上左一   内容
        self.table_title = QLabel("砝码值")
        self.g0 = QPushButton(fa5_icon, '0g')
        self.g50 = QPushButton('50g')
        self.g100 = QPushButton('100g')
        self.g150 = QPushButton('150g')
        self.g200 = QPushButton('200g')
        self.g250 = QPushButton('250g')


        self.table_value = QLabel("获取的值")
        self.g0Edit = QLineEdit('0')
        self.g50Edit = QLineEdit('0')
        self.g100Edit = QLineEdit('0')
        self.g150Edit = QLineEdit('0')
        self.g200Edit = QLineEdit('0')
        self.g250Edit = QLineEdit('0')

        self.g0.clicked.connect(self.onClick0)
        self.g50.clicked.connect(self.onClick50)
        self.g100.clicked.connect(self.onClick100)
        self.g150.clicked.connect(self.onClick150)
        self.g200.clicked.connect(self.onClick200)
        self.g250.clicked.connect(self.onClick250)
        # 上左一   布局
        self.formLayout = QFormLayout()
        self.formLayout.addRow(self.table_title, self.table_value)
        self.formLayout.addRow(self.g0,self.g0Edit)
        self.formLayout.addRow(self.g50,self.g50Edit)
        self.formLayout.addRow(self.g100,self.g100Edit)
        self.formLayout.addRow(self.g150,self.g150Edit)
        self.formLayout.addRow(self.g200,self.g200Edit)
        self.formLayout.addRow(self.g250,self.g250Edit)

        # 上左一   图本身
        self.widget1 = QWidget()
        self.widget1.setLayout(self.formLayout)
        # self.widget1.resize(300, 600)
        self.widget1.setFixedHeight(600)
        self.widget1.setFixedWidth(300)
        self.widget1.setStyleSheet('''
            QPushButton{border:none;color:black;background-color:pink;border:2px;border-radius:10px;padding:2px 4px;width:80px;height:30px}
            QLineEdit{border:2px;border-radius:10px;padding:2px 4px;width:120px;height:30px}
            QPushButton:hover{color:red}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        # 上右一   图本身
        self.widget2 = QWidget()

        # 上右一   折线图 线一
        self.series_1 = QLineSeries()  # 定义LineSerise，将类QLineSeries实例化
        self._1_point_0 = QPointF(0.00, 0.00)  # 定义折线坐标点
        self._1_point_1 = QPointF(0.80, 6.00)
        self._1_point_2 = QPointF(2.00, 2.00)
        self._1_point_3 = QPointF(4.00, 3.00)
        self._1_point_4 = QPointF(1.00, 3.00)
        self._1_point_5 = QPointF(5.00, 3.00)
        self._1_point_list = [self._1_point_0, self._1_point_1, self._1_point_4, self._1_point_2, self._1_point_3,
                              self._1_point_5]  # 定义折线点清单
        self.series_1.append(self._1_point_list)  # 折线添加坐标点清单
        self.series_1.setName("折线一")  # 折线命名

        # 上右一   折线图 线二
        self.series_2 = QLineSeries()  # 定义LineSerise，将类QLineSeries实例化
        self._2_point_0 = QPointF(0.00, 0.00)  # 定义折线坐标点
        self._2_point_1 = QPointF(0.80, 5.00)
        self._2_point_2 = QPointF(2.00, 1.00)
        self._2_point_3 = QPointF(4.00, 2.00)
        self._2_point_4 = QPointF(1.00, 2.00)
        self._2_point_5 = QPointF(5.00, 2.00)
        self._2_point_list = [self._2_point_0, self._2_point_1, self._2_point_4, self._2_point_2, self._2_point_3,
                              self._2_point_5]  # 定义折线点清单
        self.series_2.append(self._2_point_list)  # 折线添加坐标点清单
        self.series_2.setName("折线er")  # 折线命名

        self.x_Aix = QValueAxis()  # 定义x轴，实例化
        self.x_Aix.setRange(0.00, 5.00)  # 设置量程
        self.x_Aix.setLabelFormat("%0.2f")  # 设置坐标轴坐标显示方式，精确到小数点后两位
        self.x_Aix.setTickCount(6)  # 设置x轴有几个量程
        self.x_Aix.setMinorTickCount(0)  # 设置每个单元格有几个小的分级

        self.y_Aix = QValueAxis()  # 定义y轴
        self.y_Aix.setRange(0.00, 6.00)
        self.y_Aix.setLabelFormat("%0.2f")
        self.y_Aix.setTickCount(7)
        self.y_Aix.setMinorTickCount(0)

        self.charView = QChartView(self.widget2)  # 定义charView，父窗体类型为 Window
        self.charView.setGeometry(50,0, self.width(), self.height())  # 设置charView位置、大小
        self.charView.chart().addSeries(self.series_1)  # 添加折线
        self.charView.chart().addSeries(self.series_2)  # 添加折线二
        self.charView.chart().setAxisX(self.x_Aix)  # 设置x轴属性
        self.charView.chart().setAxisY(self.y_Aix)  # 设置y轴属性
        self.charView.chart().setTitleBrush(QBrush(Qt.cyan))  # 设置标题笔刷
        self.charView.chart().setTitle("信息对比图")  # 设置标题
        self.charView.show()  # 显示charView



        '''layout'''
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.widget1)
        self.hbox.addWidget(self.widget2)
        self.widget4 = QWidget()
        self.widget4.setLayout(self.hbox)

        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(QPushButton('按钮1'))
        self.hlayout.addWidget(QPushButton('按钮2'))
        self.hlayout.addWidget(QPushButton('按钮3'))
        self.hlayout.addWidget(QPushButton('按钮4'))
        self.hlayout.addWidget(QPushButton('按钮5'))
        self.hlayout.setSpacing(40)

        self.widget3 = QWidget()
        self.widget3.setLayout(self.hlayout)

        self.boxstyle = QVBoxLayout()
        self.boxstyle.addWidget(self.widget4)
        self.boxstyle.addWidget(self.widget3)
        self.setLayout(self.boxstyle)

        # 整体窗后设置
        self.setWindowTitle("串口配置工具")  # 设置题目
        self.resize(1200, 800)  # 设置长 X 宽


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qb = RadioButton()
    qb.show()
    sys.exit(app.exec_())
