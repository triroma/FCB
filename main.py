from PyQt5 import QtWidgets, Qt
import sys
from LoginWindow import LoginWindow
from RestoreWindow import RestoreWindow
from RegistrationWindow import RegistrationWindow
from MainWindow import MainWindow
import config
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox

app = QtWidgets.QApplication(sys.argv)


LoginWindow=LoginWindow()
RegistrationWindow = RegistrationWindow()
RestoreWindow=RestoreWindow()
MainWindow=MainWindow()
LoginWindow.show()

def OpenRegistrationWindows():
    RegistrationWindow.show()
    LoginWindow.close()

    def go_back():
        RegistrationWindow.close()
        LoginWindow.show()

    RegistrationWindow.cancel_btn.clicked.connect(go_back)

def OpenRestoreWindows():
    RestoreWindow.show()
    LoginWindow.close()

    def go_back():
        RestoreWindow.close()
        LoginWindow.show()

    RestoreWindow.cancel_btn.clicked.connect(go_back)

def button_click():
    global ass, bss
    ass = LoginWindow.login_input.text()
    bss = LoginWindow.password_input.text()
    shost = [LoginWindow.login_input.text(),LoginWindow.password_input.text()]
    print(shost)

def button_click1():
    LoginWindow.login_input.clear()
    LoginWindow.password_input.clear()

connection = config.getConnection()
cursor = connection.cursor()
create_table_query = "CREATE TABLE IF NOT EXISTS users (id int(3) NOT NULL AUTO_INCREMENT," \
                         "name varchar(32) DEFAULT NULL," \
                         "password varchar(32) DEFAULT NULL," \
                         "dob varchar(50) DEFAULT NULL," \
                         "PRIMARY KEY (id));"
cursor.execute(create_table_query)
def per():
    cursor = connection.cursor()
    registration_query = "Select name, password from users Where name = %s "
    cursor.execute(registration_query, (RegistrationWindow.login_input.text()))
    oneRow = cursor.fetchone()
    if oneRow == None:
        if len(RegistrationWindow.login_input.text()) < 4 or len(RegistrationWindow.password_input.text()) < 6:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Слишком короткий пароль или логин!")
            error.setInformativeText("Логин должен содержать не менее 4 символов, пароль - 6")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        elif RegistrationWindow.password_input.text() != RegistrationWindow.password_again_input.text():
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Данные в полях для ввода пароля отличаются!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        else:
            insert_query = "INSERT INTO users (name, password, dob) " \
            + "VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (RegistrationWindow.login_input.text(), RegistrationWindow.password_input.text(), RegistrationWindow.dob_dateEdit.date().toString('dd/MM/yyyy')))
            connection.commit()
            MainWindow.show()
            MainWindow.label_user.setText("<a href=\" \">{}</a>".format(RegistrationWindow.login_input.text()))
    else:
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Такая учетная запись уже существует!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()

def pur():
    cursor = connection.cursor()
    login_query = "Select name, password from users Where name = %s and password = %s"
    cursor.execute(login_query, (LoginWindow.login_input.text(), LoginWindow.password_input.text()))
    oneRow1 = cursor.fetchone()
    if oneRow1 == None:
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Пользователя с такими учетными данными не существует!")
        error.setInformativeText("Проверьте верность заполнения данных. Возможно, включен CAPSLOCK!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()
    else:
        LoginWindow.close()
        MainWindow.show()
        MainWindow.label_user.setText("<a href=\" \">{}</a>".format(LoginWindow.login_input.text()))


#def pir():


LoginWindow.registration_btn.clicked.connect(OpenRegistrationWindows)
LoginWindow.label_forgot_pass.clicked.connect(OpenRestoreWindows)
LoginWindow.login_btn.clicked.connect(pur)
LoginWindow.cancel_btn.clicked.connect(button_click1)
RegistrationWindow.sign_up_btn.clicked.connect(per)
#MainWindow.label_user.clicked.connect(pir)

#connection.close()
sys.exit(app.exec_())