from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class RestoreWindow(QMainWindow):
    def __init__(self):
        super(RestoreWindow, self).__init__()
        self.setObjectName("RestoreWindow")
        self.setFixedSize(480, 335)
        self.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_restore = QtWidgets.QLabel(self.centralwidget)
        self.label_restore.setGeometry(QtCore.QRect(70, 30, 340, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_restore.setFont(font)
        self.label_restore.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.label_restore.setAlignment(QtCore.Qt.AlignCenter)
        self.label_restore.setObjectName("label_restore")
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(70, 120, 340, 40))
        self.email_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.email_input.setObjectName("email_input")
        self.restore_password_btn = QtWidgets.QPushButton(self.centralwidget)
        self.restore_password_btn.setGeometry(QtCore.QRect(110, 180, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.restore_password_btn.setFont(font)
        self.restore_password_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.restore_password_btn.setObjectName("restore_password_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(110, 240, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.cancel_btn.setObjectName("cancel_btn")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(RestoreWindow)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, RestoreWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("RestoreWindow", "MainWindow"))
        self.label_restore.setText(_translate("RestoreWindow", "Восстановление пароля"))
        self.email_input.setPlaceholderText(_translate("RestoreWindow", "Адрес электронной почты..."))
        self.restore_password_btn.setText(_translate("RestoreWindow", "Восстановить пароль"))
        self.cancel_btn.setText(_translate("RestoreWindow", "Отмена"))

