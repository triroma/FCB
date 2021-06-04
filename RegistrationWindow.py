from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QValidator

class RegistrationWindow(QMainWindow):
    def __init__(self):
        super(RegistrationWindow, self).__init__()
        self.setObjectName("RegistrationWindow")
        self.setFixedSize(410, 540)
        self.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_registration = QtWidgets.QLabel(self.centralwidget)
        self.label_registration.setGeometry(QtCore.QRect(80, 40, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_registration.setFont(font)
        self.label_registration.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.label_registration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_registration.setObjectName("label_registration")
        self.login_input = QtWidgets.QLineEdit(self.centralwidget)
        self.login_input.setMaxLength(20)
        self.login_input.setGeometry(QtCore.QRect(50, 110, 310, 40))
        self.login_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.login_input.setObjectName("login_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setGeometry(QtCore.QRect(50, 170, 310, 40))
        self.password_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.password_input.setObjectName("password_input")
        self.password_again_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_again_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_again_input.setGeometry(QtCore.QRect(50, 230, 311, 41))
        self.password_again_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.password_again_input.setObjectName("password_again_input")
        self.label_dob = QtWidgets.QLabel(self.centralwidget)
        self.label_dob.setGeometry(QtCore.QRect(50, 330, 161, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dob.setFont(font)
        self.label_dob.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.label_dob.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dob.setObjectName("label_dob")
        self.dob_dateEdit = QtWidgets.QDateEdit(QDate.currentDate(), self.centralwidget)
        self.dob_dateEdit.setCalendarPopup(True)
        self.dob_dateEdit.setGeometry(QtCore.QRect(220, 330, 140, 40))
        self.dob_dateEdit.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.dob_dateEdit.setObjectName("dob_dateEdit")
        self.sign_up_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_btn.setGeometry(QtCore.QRect(50, 390, 310, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sign_up_btn.setFont(font)
        self.sign_up_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.sign_up_btn.setObjectName("sign_up_btn")
        self.label_registration2 = QtWidgets.QLabel(self.centralwidget)
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(50, 450, 310, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.cancel_btn.setObjectName("cancel_btn")
        self.checkBox_truesight_pass = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_truesight_pass.setGeometry(QtCore.QRect(50, 290, 150, 20))
        self.checkBox_truesight_pass.stateChanged.connect(self.checked)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_truesight_pass.setFont(font)
        self.checkBox_truesight_pass.setStyleSheet("color: rgb(186, 186, 186);")
        self.checkBox_truesight_pass.setObjectName("checkBox_truesight_pass")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("RegistrationWindow", "MainWindow"))
        self.label_registration.setText(_translate("RegistrationWindow", "Регистрация"))
        self.login_input.setPlaceholderText(_translate("RegistrationWindow", "Имя пользователя..."))
        self.password_input.setPlaceholderText(_translate("RegistrationWindow", "Пароль..."))
        self.password_again_input.setPlaceholderText(_translate("RegistrationWindow", "Повторите пароль..."))
        self.label_dob.setText(_translate("RegistrationWindow", "Дата рождения:"))
        self.sign_up_btn.setText(_translate("RegistrationWindow", "Зарегистрироваться"))
        self.cancel_btn.setText(_translate("RegistrationWindow", "Отмена"))
        self.checkBox_truesight_pass.setText(_translate("LoginWindow", "Показать пароль"))

    def checked(self):
        if self.checkBox_truesight_pass.isChecked():
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)