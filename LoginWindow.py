from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal


class QLabel_clickable(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setObjectName("LoginWindow")
        self.setFixedSize(640, 480)
        self.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(160, 50, 320, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setObjectName("label_login")
        self.login_input = QtWidgets.QLineEdit(self.centralwidget)
        self.login_input.setGeometry(QtCore.QRect(70, 140, 411, 41))
        self.login_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.login_input.setObjectName("login_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setGeometry(QtCore.QRect(70, 200, 411, 41))
        self.password_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.password_input.setObjectName("password_input")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(70, 260, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.login_btn.setObjectName("login_btn")
        self.registration_btn = QtWidgets.QPushButton(self.centralwidget)
        self.registration_btn.setGeometry(QtCore.QRect(70, 320, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.registration_btn.setFont(font)
        self.registration_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.registration_btn.setObjectName("registration_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(70, 380, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"color: rgb(186, 186, 186);")
        self.cancel_btn.setObjectName("cancel_btn")
        self.label_forgot_pass = QLabel_clickable(self)
        self.label_forgot_pass.setGeometry(QtCore.QRect(70, 440, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_forgot_pass.setFont(font)
        self.label_forgot_pass.setToolTip("")
        self.label_forgot_pass.setToolTipDuration(-1)
        self.label_forgot_pass.setStyleSheet("color: rgb(186, 186, 186);")
        self.label_forgot_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_forgot_pass.setOpenExternalLinks(True)
        self.label_forgot_pass.setObjectName("label_forgot_pass")
        self.checkBox_remember_me = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_remember_me.setGeometry(QtCore.QRect(260, 260, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_remember_me.setFont(font)
        self.checkBox_remember_me.setStyleSheet("color: rgb(186, 186, 186);")
        self.checkBox_remember_me.setObjectName("checkBox_remember_me")
        self.checkBox_truesight_pass = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_truesight_pass.setGeometry(QtCore.QRect(260, 300, 151, 21))
        self.checkBox_truesight_pass.stateChanged.connect(self.checked)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_truesight_pass.setFont(font)
        self.checkBox_truesight_pass.setStyleSheet("color: rgb(186, 186, 186);")
        self.checkBox_truesight_pass.setObjectName("checkBox_truesight_pass")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label_login.setText(_translate("LoginWindow", "Окно авторизации"))
        self.login_input.setPlaceholderText(_translate("LoginWindow", "Имя пользователя..."))
        self.password_input.setPlaceholderText(_translate("LoginWindow", "Пароль..."))
        self.login_btn.setText(_translate("LoginWindow", "Войти"))
        self.registration_btn.setText(_translate("LoginWindow", "Регистрация"))
        self.cancel_btn.setText(_translate("LoginWindow", "Отмена"))
        self.label_forgot_pass.setText(_translate("LoginWindow", "<a href=\" \">Забыли пароль?</a>"))
        self.checkBox_remember_me.setText(_translate("LoginWindow", "Запомнить меня"))
        self.checkBox_truesight_pass.setText(_translate("LoginWindow", "Показать пароль"))

    def checked(self):
        if self.checkBox_truesight_pass.isChecked():
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)







