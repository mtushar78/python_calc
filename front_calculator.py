# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    var1 = "asdfsadf"
    def setupUi(self, MainWindow):
        
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(263, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(50, 140, 31, 31))
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(lambda: self.result_textView.setText(self.btn1.text()))
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(130, 140, 31, 31))
        self.btn3.setObjectName("btn3")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(90, 140, 31, 31))
        self.btn2.setObjectName("btn2")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(50, 260, 31, 31))
        self.btn0.setObjectName("btn0")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(130, 180, 31, 31))
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(90, 180, 31, 31))
        self.btn5.setObjectName("btn5")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(50, 180, 31, 31))
        self.btn4.setObjectName("btn4")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(90, 220, 31, 31))
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(130, 220, 31, 31))
        self.btn9.setObjectName("btn9")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(50, 220, 31, 31))
        self.btn7.setObjectName("btn7")
        
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(90, 260, 31, 31))
        self.btn_dot.setObjectName("btn_dot")
        self.btn_eql = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eql.setGeometry(QtCore.QRect(130, 260, 31, 31))
        self.btn_eql.setObjectName("btn_eql")
        
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(170, 140, 31, 31))
        self.btn_div.setObjectName("btn_div")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setGeometry(QtCore.QRect(170, 260, 31, 31))
        self.btn_sub.setObjectName("btn_sub")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(170, 220, 31, 31))
        self.btn_add.setObjectName("btn_add")
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mul.setGeometry(QtCore.QRect(170, 180, 31, 31))
        self.btn_mul.setObjectName("btn_mul")
        
        self.result_textView = QtWidgets.QTextBrowser(self.centralwidget)
        self.result_textView.setGeometry(QtCore.QRect(0, 10, 261, 61))
        self.result_textView.setObjectName("result_textView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 263, 21))
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
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_eql.setText(_translate("MainWindow", "="))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_mul.setText(_translate("MainWindow", "*"))
    
    def showOnTextView(self):
        self.result_textView.setText("1")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
