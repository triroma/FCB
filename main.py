import sys
import config
from PyQt5 import QtWidgets
from LoginWindow import LoginWindow
from RestoreWindow import RestoreWindow
from RegistrationWindow import RegistrationWindow
from MainWindow import MainWindow
from NewContactWindow import NewContactWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *


#Запуск всех окон
app = QtWidgets.QApplication(sys.argv)
LoginWindow = LoginWindow()
RegistrationWindow = RegistrationWindow()
RestoreWindow = RestoreWindow()
MainWindow = MainWindow()
NewContactWindow = NewContactWindow()


def log_out():
    cursor = connection.cursor()
    update_query = "Update users set autologin = %s where name = %s"
    cursor.execute(update_query, (False, MainWindow.label_user.text()))
    connection.commit()
    MainWindow.close()
    LoginWindow.show()


def open_registration_window():
    RegistrationWindow.show()
    LoginWindow.close()

    def go_back():
        RegistrationWindow.close()
        LoginWindow.show()

    RegistrationWindow.cancel_btn.clicked.connect(go_back)


def open_restore_window():
    RestoreWindow.show()
    LoginWindow.close()

    def go_back():
        RestoreWindow.close()
        LoginWindow.show()

    RestoreWindow.cancel_btn.clicked.connect(go_back)


def clear_login_fields():
    LoginWindow.login_input.clear()
    LoginWindow.password_input.clear()


def registration():
    cursor = connection.cursor()
    registration_query = "Select name from users Where name = %s"
    cursor.execute(registration_query, (RegistrationWindow.login_input.text()))
    result_registration_query = cursor.fetchone()
    if result_registration_query == None:
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
            insert_query = "Insert INTO users (name, password, dob, autologin)" \
            + "VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (RegistrationWindow.login_input.text(), RegistrationWindow.password_input.text(), RegistrationWindow.dob_dateEdit.date().toString('yyyy-MM-dd'), False))
            connection.commit()
            MainWindow.label_user.setText(RegistrationWindow.login_input.text())
            RegistrationWindow.close()
            MainWindow.show()
    else:
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Такая учетная запись уже существует!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()


def log_in():
    cursor = connection.cursor()
    login_query = "Select name, password from users Where name = %s and password = %s"
    cursor.execute(login_query, (LoginWindow.login_input.text(), LoginWindow.password_input.text()))
    result_login_query = cursor.fetchone()
    if result_login_query == None:
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Пользователя с такими учетными данными не существует!")
        error.setInformativeText("Проверьте верность заполнения данных. Возможно, включен CAPSLOCK!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()
    else:
        if LoginWindow.checkBox_remember_me.isChecked():
            insert_query = "Update users set autologin = %s where name = %s"
            cursor.execute(insert_query, (True, LoginWindow.login_input.text()))
            connection.commit()
        elif not LoginWindow.checkBox_remember_me.isChecked():
            insert_query = "Update users set autologin = %s where name = %s"
            cursor.execute(insert_query, (False, LoginWindow.login_input.text()))
            connection.commit()
        LoginWindow.close()
        MainWindow.label_user.setText(LoginWindow.login_input.text())
        LoginWindow.login_input.clear()
        LoginWindow.password_input.clear()
        MainWindow.exit_btn.clicked.connect(log_out)
        MainWindow.show()


def open_new_contact_window():
    NewContactWindow.show()

    def go_back():
        NewContactWindow.close()

    NewContactWindow.cancel_btn.clicked.connect(go_back)


def ooo():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_2)

def oo():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_4)


def refresh():
    cursor = connection.cursor()
    refresh_query = "Select * from contacts"
    cursor.execute(refresh_query)
    result = cursor.fetchall()
    lenh = len(result)
    print(str(result))
    while lenh >= 0:
        MainWindow.tableWidget_4.removeRow(lenh)
        print(lenh)
        lenh = lenh - 1
    for item in result:
        rowPosition = MainWindow.tableWidget_4.rowCount()
        MainWindow.tableWidget_4.insertRow(rowPosition)
        MainWindow.tableWidget_4.setItem(rowPosition, 0, QTableWidgetItem(str(item["fullname"])))
        MainWindow.tableWidget_4.setItem(rowPosition, 1, QTableWidgetItem(str(item["telephone_number"])))
        MainWindow.tableWidget_4.setItem(rowPosition, 2, QTableWidgetItem(str(item["dob"])))


def add_new_contact():
    cursor = connection.cursor()
    info_check_query = "Select fullname from contacts Where fullname = %s and telephone_number = %s and dob = %s"
    cursor.execute(info_check_query, (NewContactWindow.name_input.text(), NewContactWindow.telephone_number_input.text(), NewContactWindow.dob_dateEdit.date().toString('yyyy-MM-dd')))
    result_info_check_query = cursor.fetchone()
    if result_info_check_query == None:
        insert_query = "Insert INTO contacts (fullname, telephone_number, dob)" \
                       + "VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (NewContactWindow.name_input.text(), NewContactWindow.telephone_number_input.text(), NewContactWindow.dob_dateEdit.date().toString('yyyy-MM-dd')))
        connection.commit()
        success = QMessageBox()
        success.setWindowTitle("Успех!!!")
        success.setText("Контакт успешно добавлен!")
        success.setStandardButtons(QMessageBox.Ok)
        success.exec_()
    else:
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Контакт с введенными данными уже существует!")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()


#Первый коннект к бд. Создание таблиц: users(пользователи программы) и contacts(контакты).
connection = config.getConnection()


cursor = connection.cursor()
create_table_query = "CREATE TABLE IF NOT EXISTS users (id int(5) NOT NULL AUTO_INCREMENT," \
                         "name varchar(20) DEFAULT NULL," \
                         "password varchar(20) DEFAULT NULL," \
                         "dob date DEFAULT NULL," \
                         "autologin bool DEFAULT NULL," \
                         "PRIMARY KEY (id));"
cursor.execute(create_table_query)
cursor = connection.cursor()
create_table_query = "CREATE TABLE IF NOT EXISTS contacts (id int(5) NOT NULL AUTO_INCREMENT," \
                         "fullname varchar(32) DEFAULT NULL," \
                         "telephone_number varchar(32) DEFAULT NULL," \
                         "dob date DEFAULT NULL," \
                         "PRIMARY KEY (id));"
cursor.execute(create_table_query)

#Чек на пустую бд.
connection = config.getConnection()
cursor = connection.cursor()
first_query = "SELECT (CASE WHEN NOT EXISTS(SELECT NULL FROM users) THEN 1 ELSE 0 END) AS isEmpty;"
cursor.execute(first_query)
result_first_query = int(cursor.fetchone()["isEmpty"])
if result_first_query == 1:
    LoginWindow.show()
elif result_first_query == 0:
    cursor = connection.cursor()
    autologin_query = "Select name from users Where autologin = %s"
    cursor.execute(autologin_query, True)
    result_autologin_query = cursor.fetchone()
    if result_autologin_query == None:
        LoginWindow.show()
    else:
        MainWindow.label_user.setText(str(result_autologin_query["name"]))
        MainWindow.exit_btn.clicked.connect(log_out)
        MainWindow.New_btn.clicked.connect(open_new_contact_window)
        NewContactWindow.add_btn.clicked.connect(add_new_contact)
        MainWindow.delete_btn.clicked.connect(refresh)
        MainWindow.pushButton_1.clicked.connect(ooo)
        MainWindow.pushButton_2.clicked.connect(oo)
        MainWindow.show()


LoginWindow.registration_btn.clicked.connect(open_registration_window)
LoginWindow.label_forgot_pass.clicked.connect(open_restore_window)
LoginWindow.login_btn.clicked.connect(log_in)
LoginWindow.cancel_btn.clicked.connect(clear_login_fields)
RegistrationWindow.sign_up_btn.clicked.connect(registration)
MainWindow.New_btn.clicked.connect(open_new_contact_window)


sys.exit(app.exec_())
connection.close()