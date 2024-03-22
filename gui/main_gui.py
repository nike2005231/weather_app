from PyQt5 import QtCore, QtGui, QtWidgets
import click_handler

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 746)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 610, 211, 51))

        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(14)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(
            lambda: click_handler.click_button(
                self.lineEdit, self.info_city, 
                self.fill_1, self.fill_2, self.fill_3, self.fill_4, 
                self.temp_1, self.temp_2, self.temp_3, self.temp_4,
                self.wet_1, self.wet_2, self.wet_3, self.wet_4,
                self.brezee_1, self.brezee_2, self.brezee_3, self.brezee_4
                )
            )

        self.label_city = QtWidgets.QLabel(self.centralwidget)
        self.label_city.setGeometry(QtCore.QRect(480, 500, 71, 41))
        self.label_city.setSizeIncrement(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.label_city.setFont(font)
        self.label_city.setObjectName("label_city")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 550, 511, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.night = QtWidgets.QLabel(self.centralwidget)
        self.night.setGeometry(QtCore.QRect(60, 150, 101, 41))
        self.night.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.night.setFont(font)
        self.night.setObjectName("night")

        self.morning = QtWidgets.QLabel(self.centralwidget)
        self.morning.setGeometry(QtCore.QRect(60, 240, 101, 41))
        self.morning.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.morning.setFont(font)
        self.morning.setObjectName("morning")

        self.day = QtWidgets.QLabel(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(60, 330, 101, 41))
        self.day.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.day.setFont(font)
        self.day.setObjectName("day")

        self.eving = QtWidgets.QLabel(self.centralwidget)
        self.eving.setGeometry(QtCore.QRect(60, 430, 101, 41))
        self.eving.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.eving.setFont(font)
        self.eving.setObjectName("eving")

        self.temp_1 = QtWidgets.QLabel(self.centralwidget)
        self.temp_1.setGeometry(QtCore.QRect(180, 150, 181, 41))
        self.temp_1.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.temp_1.setFont(font)
        self.temp_1.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_1.setObjectName("temp_1")

        self.temp_2 = QtWidgets.QLabel(self.centralwidget)
        self.temp_2.setGeometry(QtCore.QRect(180, 240, 181, 41))
        self.temp_2.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.temp_2.setFont(font)
        self.temp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_2.setObjectName("temp_2")

        self.temp_3 = QtWidgets.QLabel(self.centralwidget)
        self.temp_3.setGeometry(QtCore.QRect(180, 330, 181, 41))
        self.temp_3.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.temp_3.setFont(font)
        self.temp_3.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_3.setObjectName("temp_3")

        self.temp_4 = QtWidgets.QLabel(self.centralwidget)
        self.temp_4.setGeometry(QtCore.QRect(180, 430, 181, 41))
        self.temp_4.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.temp_4.setFont(font)
        self.temp_4.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_4.setObjectName("temp_4")

        self.fill_1 = QtWidgets.QLabel(self.centralwidget)
        self.fill_1.setGeometry(QtCore.QRect(410, 150, 181, 41))
        self.fill_1.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.fill_1.setFont(font)
        self.fill_1.setAlignment(QtCore.Qt.AlignCenter)
        self.fill_1.setObjectName("fill_1")

        self.fill_2 = QtWidgets.QLabel(self.centralwidget)
        self.fill_2.setGeometry(QtCore.QRect(410, 240, 181, 41))
        self.fill_2.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.fill_2.setFont(font)
        self.fill_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fill_2.setObjectName("fill_2")

        self.fill_3 = QtWidgets.QLabel(self.centralwidget)
        self.fill_3.setGeometry(QtCore.QRect(410, 330, 181, 41))
        self.fill_3.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.fill_3.setFont(font)
        self.fill_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fill_3.setObjectName("fill_3")

        self.fill_4 = QtWidgets.QLabel(self.centralwidget)
        self.fill_4.setGeometry(QtCore.QRect(410, 430, 181, 41))
        self.fill_4.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.fill_4.setFont(font)
        self.fill_4.setAlignment(QtCore.Qt.AlignCenter)
        self.fill_4.setObjectName("fill_4")

        self.brezee_1 = QtWidgets.QLabel(self.centralwidget)
        self.brezee_1.setGeometry(QtCore.QRect(600, 150, 171, 41))
        self.brezee_1.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.brezee_1.setFont(font)
        self.brezee_1.setAlignment(QtCore.Qt.AlignCenter)
        self.brezee_1.setObjectName("brezee_1")

        self.wet_1 = QtWidgets.QLabel(self.centralwidget)
        self.wet_1.setGeometry(QtCore.QRect(800, 150, 181, 41))
        self.wet_1.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)

        self.wet_1.setFont(font)
        self.wet_1.setAlignment(QtCore.Qt.AlignCenter)
        self.wet_1.setObjectName("wet_1")

        self.wet_2 = QtWidgets.QLabel(self.centralwidget)
        self.wet_2.setGeometry(QtCore.QRect(800, 240, 181, 41))
        self.wet_2.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.wet_2.setFont(font)
        self.wet_2.setAlignment(QtCore.Qt.AlignCenter)
        self.wet_2.setObjectName("wet_2")

        self.wet_3 = QtWidgets.QLabel(self.centralwidget)
        self.wet_3.setGeometry(QtCore.QRect(800, 330, 181, 41))
        self.wet_3.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.wet_3.setFont(font)
        self.wet_3.setAlignment(QtCore.Qt.AlignCenter)
        self.wet_3.setObjectName("wet_3")

        self.wet_4 = QtWidgets.QLabel(self.centralwidget)
        self.wet_4.setGeometry(QtCore.QRect(800, 430, 181, 41))
        self.wet_4.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.wet_4.setFont(font)
        self.wet_4.setAlignment(QtCore.Qt.AlignCenter)
        self.wet_4.setObjectName("wet_4")

        self.it_fill_like = QtWidgets.QLabel(self.centralwidget)
        self.it_fill_like.setGeometry(QtCore.QRect(410, 80, 181, 41))
        self.it_fill_like.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.it_fill_like.setFont(font)
        self.it_fill_like.setObjectName("it_fill_like")
        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(180, 80, 181, 41))
        self.temperature.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.temperature.setFont(font)
        self.temperature.setObjectName("temperature")

        self.brezee = QtWidgets.QLabel(self.centralwidget)
        self.brezee.setGeometry(QtCore.QRect(640, 80, 81, 41))
        self.brezee.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.brezee.setFont(font)
        self.brezee.setObjectName("brezee")

        self.wet = QtWidgets.QLabel(self.centralwidget)
        self.wet.setGeometry(QtCore.QRect(820, 80, 151, 41))
        self.wet.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.wet.setFont(font)
        self.wet.setObjectName("wet")

        self.brezee_2 = QtWidgets.QLabel(self.centralwidget)
        self.brezee_2.setGeometry(QtCore.QRect(600, 240, 171, 41))
        self.brezee_2.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.brezee_2.setFont(font)
        self.brezee_2.setAlignment(QtCore.Qt.AlignCenter)
        self.brezee_2.setObjectName("brezee_2")

        self.brezee_3 = QtWidgets.QLabel(self.centralwidget)
        self.brezee_3.setGeometry(QtCore.QRect(600, 330, 171, 41))
        self.brezee_3.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.brezee_3.setFont(font)
        self.brezee_3.setAlignment(QtCore.Qt.AlignCenter)
        self.brezee_3.setObjectName("brezee_3")

        self.brezee_4 = QtWidgets.QLabel(self.centralwidget)
        self.brezee_4.setGeometry(QtCore.QRect(600, 430, 171, 41))
        self.brezee_4.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.brezee_4.setFont(font)
        self.brezee_4.setAlignment(QtCore.Qt.AlignCenter)
        self.brezee_4.setObjectName("brezee_4")

        self.info_city = QtWidgets.QLabel(self.centralwidget)
        self.info_city.setGeometry(QtCore.QRect(10, 20, 1011, 41))
        self.info_city.setSizeIncrement(QtCore.QSize(10, 0))

        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.info_city.setFont(font)
        self.info_city.setAlignment(QtCore.Qt.AlignCenter)
        self.info_city.setObjectName("info_city")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label_city.setText(_translate("MainWindow", "City"))
        self.night.setText(_translate("MainWindow", "Ночь"))
        self.morning.setText(_translate("MainWindow", "Утро"))
        self.day.setText(_translate("MainWindow", "День"))
        self.eving.setText(_translate("MainWindow", "Вечер"))
        self.temp_1.setText(_translate("MainWindow", ""))
        self.temp_2.setText(_translate("MainWindow", ""))
        self.temp_3.setText(_translate("MainWindow", ""))
        self.temp_4.setText(_translate("MainWindow", ""))
        self.fill_1.setText(_translate("MainWindow", ""))
        self.fill_2.setText(_translate("MainWindow", ""))
        self.fill_3.setText(_translate("MainWindow", ""))
        self.fill_4.setText(_translate("MainWindow", ""))
        self.brezee_1.setText(_translate("MainWindow", ""))
        self.wet_1.setText(_translate("MainWindow", ""))
        self.wet_2.setText(_translate("MainWindow", ""))
        self.wet_3.setText(_translate("MainWindow", ""))
        self.wet_4.setText(_translate("MainWindow", ""))
        self.it_fill_like.setText(_translate("MainWindow", "Ощущаеться"))
        self.temperature.setText(_translate("MainWindow", "Температура"))
        self.brezee.setText(_translate("MainWindow", "Ветер"))
        self.wet.setText(_translate("MainWindow", "Влажность"))
        self.brezee_2.setText(_translate("MainWindow", ""))
        self.brezee_3.setText(_translate("MainWindow", ""))
        self.brezee_4.setText(_translate("MainWindow", ""))
        self.info_city.setText(_translate("MainWindow", ""))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
