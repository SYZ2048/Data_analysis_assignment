# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from system_menu import Ui_MainWindow
from PyQt5.QtCore import Qt
from data_analysis import average_price, number_proportion, house_decoration, type_average_price, price_prediction
import threading


class MyPyQT_Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.setupUi(self)

    # 各区二手房均价分析
    @staticmethod
    def act1_average_price(self):
        average_price()
        # print("hi")

    # 各区二手房数量所占比例
    @staticmethod
    def act2_number_proportion(self):
        number_proportion()
        # print("2")

    # 全市二手房装修程度分析
    @staticmethod
    def act3_house_decoration(self):
        house_decoration()
        # print("3")

    # 热门户型均价分析
    @staticmethod
    def act4_type_average_price(self):
        type_average_price()
        # print("4")

    # 二手房售价预测
    @staticmethod
    def act5_price_prediction(self):
        price_prediction()
        # print("5")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)   # 启用或禁用高DPI缩放
    my_pyqt_form = MyPyQT_Form()

    my_pyqt_form.action_1.triggered.connect(my_pyqt_form.act1_average_price)
    my_pyqt_form.action_2.triggered.connect(my_pyqt_form.act2_number_proportion)
    my_pyqt_form.action_3.triggered.connect(my_pyqt_form.act3_house_decoration)
    my_pyqt_form.action_4.triggered.connect(my_pyqt_form.act4_type_average_price)
    my_pyqt_form.action_5.triggered.connect(my_pyqt_form.act5_price_prediction)

    my_pyqt_form.show()
    sys.exit(app.exec_())
