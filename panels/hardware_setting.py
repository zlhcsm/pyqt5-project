# QDesktopWidget
import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication,QWidget,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class HardwarePanel(QWidget):
    def __init__(self):
        super(HardwarePanel,self).__init__()

        # 设置主窗口的标题
        hlayout = QHBoxLayout()
        set_DAC_but = QPushButton('设置DAC值')
        set_DAC_line = QLineEdit('0')
        cur_ADC = QPushButton('当前ADC值')
        cur_DAC = QPushButton('当前DAC值')
        cur_TOCO = QPushButton('当前TOCO值')

        hlayout.addWidget(set_DAC_but)
        hlayout.addWidget(set_DAC_line)
        hlayout.addWidget(cur_ADC)
        hlayout.addWidget(cur_TOCO)
        hlayout.setSpacing(40)
        self.setLayout(hlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HardwarePanel()
    main.show()
    sys.exit(app.exec_())