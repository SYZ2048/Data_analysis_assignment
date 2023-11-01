# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from system_menu import Ui_MainWindow
from PyQt5.QtCore import Qt


class MyPyQT_Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)

    # 实现pushButton_click()函数，textEdit是我们放上去的文本框的id
    # def pushButton_click_test(self):
    #     self.textEdit.setText("你点击了按钮")

    # 各区二手房均价分析
    @staticmethod
    def average_price(self):
        print("hi")

    # 各区二手房数量所占比例
    @staticmethod
    def number_proportion(self):
        print("2")

    # 全市二手房装修程度分析
    @staticmethod
    def house_decoration(self):
        print("3")

    # 热门户型均价分析
    @staticmethod
    def type_average_price(self):
        print("4")

    # 二手房售价预测
    @staticmethod
    def price_prediction(self):
        print("5")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)   # 启用或禁用高DPI缩放
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.action_1.triggered.connect(my_pyqt_form.average_price)

    my_pyqt_form.show()
    sys.exit(app.exec_())
