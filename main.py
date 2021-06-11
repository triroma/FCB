import sys
import config
from PyQt5 import QtWidgets
from LoginWindow import LoginWindow
from RestoreWindow import RestoreWindow
from RegistrationWindow import RegistrationWindow
from MainWindow import MainWindow
from NewContactWindow import NewContactWindow
from EditWindow import EditWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


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
    if result_registration_query is None:
        if len(RegistrationWindow.login_input.text()) < 4 or len(RegistrationWindow.password_input.text()) < 6:
            error_low_len = QMessageBox()
            font = QtGui.QFont()
            font.setPointSize(18)
            error_low_len.setFont(font)
            error_low_len.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                        "color: rgb(186, 186, 186);")
            error_low_len.setWindowTitle("Ошибка!")
            error_low_len.setText("Слишком короткий пароль или логин!")
            error_low_len.setInformativeText("Логин должен содержать не менее 4 символов, пароль - 6")
            error_low_len.setIcon(QMessageBox.Warning)
            error_low_len.setStandardButtons(QMessageBox.Ok)
            error_low_len.exec_()
        elif RegistrationWindow.password_input.text() != RegistrationWindow.password_again_input.text():
            error_different_value = QMessageBox()
            font = QtGui.QFont()
            font.setPointSize(18)
            error_different_value.setFont(font)
            error_different_value.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                                "color: rgb(186, 186, 186);")
            error_different_value.setWindowTitle("Ошибка!")
            error_different_value.setText("Данные в полях для ввода пароля отличаются!")
            error_different_value.setIcon(QMessageBox.Warning)
            error_different_value.setStandardButtons(QMessageBox.Ok)
            error_different_value.exec_()
        else:
            insert_query = "Insert INTO users (name, password, dob, autologin)" \
                           + "VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (RegistrationWindow.login_input.text(),
                                          RegistrationWindow.password_input.text(),
                                          RegistrationWindow.dob_dateEdit.date().toString('yyyy-MM-dd'), False))
            connection.commit()
            MainWindow.label_user.setText(RegistrationWindow.login_input.text())
            RegistrationWindow.close()
            MainWindow.show()
    else:
        error_existing_login = QMessageBox()
        font = QtGui.QFont()
        font.setPointSize(18)
        error_existing_login.setFont(font)
        error_existing_login.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                           "color: rgb(186, 186, 186);")
        error_existing_login.setWindowTitle("Ошибка!")
        error_existing_login.setText("Такая учетная запись уже существует!")
        error_existing_login.setIcon(QMessageBox.Warning)
        error_existing_login.setStandardButtons(QMessageBox.Ok)
        error_existing_login.exec_()


def log_in():
    cursor = connection.cursor()
    login_query = "Select name, password from users Where name = %s and password = %s"
    cursor.execute(login_query, (LoginWindow.login_input.text(), LoginWindow.password_input.text()))
    result_login_query = cursor.fetchone()
    if result_login_query is None:
        error_missmatch_login = QMessageBox()
        font = QtGui.QFont()
        font.setPointSize(18)
        error_missmatch_login.setFont(font)
        error_missmatch_login.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                            "color: rgb(186, 186, 186);")
        error_missmatch_login.setWindowTitle("Ошибка!")
        error_missmatch_login.setText("Пользователя с такими учетными данными не существует!")
        error_missmatch_login.setInformativeText("Проверьте верность заполнения данных. Возможно, включен CAPSLOCK!")
        error_missmatch_login.setIcon(QMessageBox.Warning)
        error_missmatch_login.setStandardButtons(QMessageBox.Ok)
        error_missmatch_login.exec_()
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
        notification()
        refresh()
        MainWindow.show()


def open_new_contact_window():
    NewContactWindow.show()

    def go_back():
        NewContactWindow.close()

    NewContactWindow.cancel_btn.clicked.connect(go_back)


def changed_to_1page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_1)


def changed_to_2page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_2)


def changed_to_3page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_3)


def changed_to_4page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_4)


def changed_to_5page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_5)


def changed_to_6page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_6)


def changed_to_7page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_7)


def changed_to_8page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_8)


def changed_to_9page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_9)


def changed_to_10page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_10)


def changed_to_11page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_11)


def changed_to_12page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_12)


def changed_to_13page():
    MainWindow.stackedWidget.setCurrentWidget(MainWindow.page_13)


def refresh():
    cursor = connection.cursor()
    refresh_query = "Select * from contacts"
    cursor.execute(refresh_query)
    resulting = cursor.fetchall()
    MainWindow.tableWidget_1.setRowCount(0)
    MainWindow.tableWidget_2.setRowCount(0)
    MainWindow.tableWidget_3.setRowCount(0)
    MainWindow.tableWidget_4.setRowCount(0)
    MainWindow.tableWidget_5.setRowCount(0)
    MainWindow.tableWidget_6.setRowCount(0)
    MainWindow.tableWidget_7.setRowCount(0)
    MainWindow.tableWidget_8.setRowCount(0)
    MainWindow.tableWidget_9.setRowCount(0)
    MainWindow.tableWidget_10.setRowCount(0)
    MainWindow.tableWidget_11.setRowCount(0)
    MainWindow.tableWidget_12.setRowCount(0)
    MainWindow.tableWidget_13.setRowCount(0)
    for item in resulting:
        if str(item["fullname"])[:1].lower().startswith("а") or str(item["fullname"])[:1].lower().startswith("б"):
            row_position = MainWindow.tableWidget_1.rowCount()
            MainWindow.tableWidget_1.insertRow(row_position)
            MainWindow.tableWidget_1.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_1.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_1.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("в") or str(item["fullname"])[:1].lower().startswith("г"):
            row_position = MainWindow.tableWidget_2.rowCount()
            MainWindow.tableWidget_2.insertRow(row_position)
            MainWindow.tableWidget_2.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_2.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_2.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("д") or str(item["fullname"])[:1].lower().startswith("е"):
            row_position = MainWindow.tableWidget_3.rowCount()
            MainWindow.tableWidget_3.insertRow(row_position)
            MainWindow.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("ж") or str(item["fullname"])[:1].lower().startswith("з") or \
                str(item["fullname"])[:1].lower().startswith("и") or str(item["fullname"])[:1].lower().startswith("й"):
            row_position = MainWindow.tableWidget_4.rowCount()
            MainWindow.tableWidget_4.insertRow(row_position)
            MainWindow.tableWidget_4.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_4.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_4.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("к") or str(item["fullname"])[:1].lower().startswith("л"):
            row_position = MainWindow.tableWidget_5.rowCount()
            MainWindow.tableWidget_5.insertRow(row_position)
            MainWindow.tableWidget_5.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_5.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_5.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("м") or str(item["fullname"])[:1].lower().startswith("н"):
            row_position = MainWindow.tableWidget_6.rowCount()
            MainWindow.tableWidget_6.insertRow(row_position)
            MainWindow.tableWidget_6.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_6.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_6.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("о") or str(item["fullname"])[:1].lower().startswith("п"):
            row_position = MainWindow.tableWidget_7.rowCount()
            MainWindow.tableWidget_7.insertRow(row_position)
            MainWindow.tableWidget_7.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_7.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_7.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("р") or str(item["fullname"])[:1].lower().startswith("с"):
            row_position = MainWindow.tableWidget_8.rowCount()
            MainWindow.tableWidget_8.insertRow(row_position)
            MainWindow.tableWidget_8.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_8.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_8.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("т") or str(item["fullname"])[:1].lower().startswith("у"):
            row_position = MainWindow.tableWidget_9.rowCount()
            MainWindow.tableWidget_9.insertRow(row_position)
            MainWindow.tableWidget_9.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_9.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_9.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("ф") or str(item["fullname"])[:1].lower().startswith("х"):
            row_position = MainWindow.tableWidget_10.rowCount()
            MainWindow.tableWidget_10.insertRow(row_position)
            MainWindow.tableWidget_10.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_10.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_10.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("ц") or str(item["fullname"])[:1].lower().startswith("ч") or \
                str(item["fullname"])[:1].lower().startswith("ш") or str(item["fullname"])[:1].lower().startswith("щ"):
            row_position = MainWindow.tableWidget_11.rowCount()
            MainWindow.tableWidget_11.insertRow(row_position)
            MainWindow.tableWidget_11.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_11.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_11.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("ъ") or str(item["fullname"])[:1].lower().startswith("ы") or \
                str(item["fullname"])[:1].lower().startswith("ь") or str(item["fullname"])[:1].lower().startswith("э"):
            row_position = MainWindow.tableWidget_12.rowCount()
            MainWindow.tableWidget_12.insertRow(row_position)
            MainWindow.tableWidget_12.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_12.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_12.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))
        if str(item["fullname"])[:1].lower().startswith("ю") or str(item["fullname"])[:1].lower().startswith("я"):
            row_position = MainWindow.tableWidget_13.rowCount()
            MainWindow.tableWidget_13.insertRow(row_position)
            MainWindow.tableWidget_13.setItem(row_position, 0, QTableWidgetItem(str(item["fullname"])))
            MainWindow.tableWidget_13.setItem(row_position, 1, QTableWidgetItem(str(item["telephone_number"])))
            MainWindow.tableWidget_13.setItem(row_position, 2, QTableWidgetItem(str(item["dob"])))


def add_new_contact():
    cursor = connection.cursor()
    info_check_query = "Select fullname from contacts Where fullname = %s and telephone_number = %s and dob = %s"
    cursor.execute(info_check_query, (NewContactWindow.name_input.text(),
                                      NewContactWindow.telephone_number_input.text(),
                                      NewContactWindow.dob_dateEdit.date().toString('yyyy-MM-dd')))
    result_info_check_query = cursor.fetchone()
    if result_info_check_query is None:
        if len(NewContactWindow.name_input.text()) > 1 and len(NewContactWindow.telephone_number_input.text()) > 5:
            insert_query = "Insert INTO contacts (fullname, telephone_number, dob)" \
                           + "VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (NewContactWindow.name_input.text(),
                                          NewContactWindow.telephone_number_input.text(),
                                          NewContactWindow.dob_dateEdit.date().toString('yyyy-MM-dd')))
            connection.commit()
            success = QMessageBox()
            font = QtGui.QFont()
            font.setPointSize(18)
            success.setFont(font)
            success.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                  "color: rgb(186, 186, 186);")
            success.setWindowTitle("Успех!!!")
            success.setText("Контакт успешно добавлен!")
            success.setStandardButtons(QMessageBox.Ok)
            success.exec_()
            NewContactWindow.name_input.clear()
            NewContactWindow.telephone_number_input.clear()
            NewContactWindow.dob_dateEdit.clear()
            NewContactWindow.close()
        else:
            edit_error = QMessageBox()
            font = QtGui.QFont()
            font.setPointSize(18)
            edit_error.setFont(font)
            edit_error.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                     "color: rgb(186, 186, 186);")
            edit_error.setWindowTitle("Ошибка!")
            edit_error.setText("Имя контакта должно содержать не менее 2-х символов, номер телефона - 6-ти.")
            edit_error.setStandardButtons(QMessageBox.Ok)
            edit_error.exec_()
    else:
        error_same_contact = QMessageBox()
        font = QtGui.QFont()
        font.setPointSize(18)
        error_same_contact.setFont(font)
        error_same_contact.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                         "color: rgb(186, 186, 186);")
        error_same_contact.setWindowTitle("Ошибка!")
        error_same_contact.setText("Контакт с введенными данными уже существует!")
        error_same_contact.setIcon(QMessageBox.Warning)
        error_same_contact.setStandardButtons(QMessageBox.Ok)
        error_same_contact.exec_()


def successful_editing():
    event = QMessageBox()
    font = QtGui.QFont()
    font.setPointSize(18)
    event.setFont(font)
    event.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                        "color: rgb(186, 186, 186);")
    event.setWindowTitle("Успех!!")
    event.setText("Данные успешно отредактированы!")
    event.setIcon(QMessageBox.Warning)
    event.setStandardButtons(QMessageBox.Ok)
    event.exec_()
    EditWindow.close()


def delete_contact():
    if MainWindow.tableWidget_1.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_1.currentRow()
        column = MainWindow.tableWidget_1.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_1.item(row, column).text(),
                                          MainWindow.tableWidget_1.item(row, column+1).text(),
                                          MainWindow.tableWidget_1.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_1.item(row, column-1).text(),
                                          MainWindow.tableWidget_1.item(row, column).text(),
                                          MainWindow.tableWidget_1.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_1.item(row, column-2).text(),
                                          MainWindow.tableWidget_1.item(row, column-1).text(),
                                          MainWindow.tableWidget_1.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_2.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_2.currentRow()
        column = MainWindow.tableWidget_2.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_2.item(row, column).text(),
                                          MainWindow.tableWidget_2.item(row, column+1).text(),
                                          MainWindow.tableWidget_2.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_2.item(row, column-1).text(),
                                          MainWindow.tableWidget_2.item(row, column).text(),
                                          MainWindow.tableWidget_2.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_2.item(row, column-2).text(),
                                          MainWindow.tableWidget_2.item(row, column-1).text(),
                                          MainWindow.tableWidget_2.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_3.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_3.currentRow()
        column = MainWindow.tableWidget_3.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_3.item(row, column).text(),
                                          MainWindow.tableWidget_3.item(row, column+1).text(),
                                          MainWindow.tableWidget_3.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_3.item(row, column-1).text(),
                                          MainWindow.tableWidget_3.item(row, column).text(),
                                          MainWindow.tableWidget_3.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_3.item(row, column-2).text(),
                                          MainWindow.tableWidget_3.item(row, column-1).text(),
                                          MainWindow.tableWidget_3.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_4.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_4.currentRow()
        column = MainWindow.tableWidget_4.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_4.item(row, column).text(),
                                          MainWindow.tableWidget_4.item(row, column+1).text(),
                                          MainWindow.tableWidget_4.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_4.item(row, column-1).text(),
                                          MainWindow.tableWidget_4.item(row, column).text(),
                                          MainWindow.tableWidget_4.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_4.item(row, column-2).text(),
                                          MainWindow.tableWidget_4.item(row, column-1).text(),
                                          MainWindow.tableWidget_4.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_5.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_5.currentRow()
        column = MainWindow.tableWidget_5.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_5.item(row, column).text(),
                                          MainWindow.tableWidget_5.item(row, column+1).text(),
                                          MainWindow.tableWidget_5.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_5.item(row, column-1).text(),
                                          MainWindow.tableWidget_5.item(row, column).text(),
                                          MainWindow.tableWidget_5.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_5.item(row, column-2).text(),
                                          MainWindow.tableWidget_5.item(row, column-1).text(),
                                          MainWindow.tableWidget_5.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_6.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_6.currentRow()
        column = MainWindow.tableWidget_6.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_6.item(row, column).text(),
                                          MainWindow.tableWidget_6.item(row, column+1).text(),
                                          MainWindow.tableWidget_6.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_6.item(row, column-1).text(),
                                          MainWindow.tableWidget_6.item(row, column).text(),
                                          MainWindow.tableWidget_6.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_6.item(row, column-2).text(),
                                          MainWindow.tableWidget_6.item(row, column-1).text(),
                                          MainWindow.tableWidget_6.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_7.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_7.currentRow()
        column = MainWindow.tableWidget_7.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_7.item(row, column).text(),
                                          MainWindow.tableWidget_7.item(row, column+1).text(),
                                          MainWindow.tableWidget_7.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_7.item(row, column-1).text(),
                                          MainWindow.tableWidget_7.item(row, column).text(),
                                          MainWindow.tableWidget_7.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_7.item(row, column-2).text(),
                                          MainWindow.tableWidget_7.item(row, column-1).text(),
                                          MainWindow.tableWidget_7.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_8.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_8.currentRow()
        column = MainWindow.tableWidget_8.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_8.item(row, column).text(),
                                          MainWindow.tableWidget_8.item(row, column+1).text(),
                                          MainWindow.tableWidget_8.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_8.item(row, column-1).text(),
                                          MainWindow.tableWidget_8.item(row, column).text(),
                                          MainWindow.tableWidget_8.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_8.item(row, column-2).text(),
                                          MainWindow.tableWidget_8.item(row, column-1).text(),
                                          MainWindow.tableWidget_8.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_9.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_9.currentRow()
        column = MainWindow.tableWidget_9.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_9.item(row, column).text(),
                                          MainWindow.tableWidget_9.item(row, column+1).text(),
                                          MainWindow.tableWidget_9.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_9.item(row, column-1).text(),
                                          MainWindow.tableWidget_9.item(row, column).text(),
                                          MainWindow.tableWidget_9.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_9.item(row, column-2).text(),
                                          MainWindow.tableWidget_9.item(row, column-1).text(),
                                          MainWindow.tableWidget_9.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_10.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_10.currentRow()
        column = MainWindow.tableWidget_10.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_10.item(row, column).text(),
                                          MainWindow.tableWidget_10.item(row, column+1).text(),
                                          MainWindow.tableWidget_10.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_10.item(row, column-1).text(),
                                          MainWindow.tableWidget_10.item(row, column).text(),
                                          MainWindow.tableWidget_10.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_10.item(row, column-2).text(),
                                          MainWindow.tableWidget_10.item(row, column-1).text(),
                                          MainWindow.tableWidget_10.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_11.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_11.currentRow()
        column = MainWindow.tableWidget_11.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_11.item(row, column).text(),
                                          MainWindow.tableWidget_11.item(row, column+1).text(),
                                          MainWindow.tableWidget_11.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_11.item(row, column-1).text(),
                                          MainWindow.tableWidget_11.item(row, column).text(),
                                          MainWindow.tableWidget_11.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_11.item(row, column-2).text(),
                                          MainWindow.tableWidget_11.item(row, column-1).text(),
                                          MainWindow.tableWidget_11.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_12.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_12.currentRow()
        column = MainWindow.tableWidget_12.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_12.item(row, column).text(),
                                          MainWindow.tableWidget_12.item(row, column+1).text(),
                                          MainWindow.tableWidget_12.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_12.item(row, column-1).text(),
                                          MainWindow.tableWidget_12.item(row, column).text(),
                                          MainWindow.tableWidget_12.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_12.item(row, column-2).text(),
                                          MainWindow.tableWidget_12.item(row, column-1).text(),
                                          MainWindow.tableWidget_12.item(row, column).text()))
            connection.commit()
    if MainWindow.tableWidget_13.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_13.currentRow()
        column = MainWindow.tableWidget_13.currentColumn()
        if column == 0:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_13.item(row, column).text(),
                                          MainWindow.tableWidget_13.item(row, column+1).text(),
                                          MainWindow.tableWidget_13.item(row, column+2).text()))
            connection.commit()
        if column == 1:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_13.item(row, column-1).text(),
                                          MainWindow.tableWidget_13.item(row, column).text(),
                                          MainWindow.tableWidget_13.item(row, column+1).text()))
            connection.commit()
        if column == 2:
            delete_query = "Delete from contacts where fullname = %s and telephone_number = %s and dob = %s"
            cursor.execute(delete_query, (MainWindow.tableWidget_13.item(row, column-2).text(),
                                          MainWindow.tableWidget_13.item(row, column-1).text(),
                                          MainWindow.tableWidget_13.item(row, column).text()))
            connection.commit()
    successful_deletion()
    EditWindow.close()


def open_edit_data_window():
    EditWindow.show()


def few_characters():
    few_characters_message = QMessageBox()
    font = QtGui.QFont()
    font.setPointSize(18)
    few_characters_message.setFont(font)
    few_characters_message.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                         "color: rgb(186, 186, 186);")
    few_characters_message.setWindowTitle("Ошибка!")
    few_characters_message.setText("Редактирумое поле должно содержать более 2-х символов!")
    few_characters_message.setIcon(QMessageBox.Warning)
    few_characters_message.setStandardButtons(QMessageBox.Ok)
    few_characters_message.exec_()


def successful_deletion():
    delete_contact_message = QMessageBox()
    font = QtGui.QFont()
    font.setPointSize(18)
    delete_contact_message.setFont(font)
    delete_contact_message.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                         "color: rgb(186, 186, 186);")
    delete_contact_message.setWindowTitle("Удаление контакта!")
    delete_contact_message.setText("Контакт успешно удален!")
    delete_contact_message.setIcon(QMessageBox.Warning)
    delete_contact_message.setStandardButtons(QMessageBox.Ok)
    delete_contact_message.exec_()


def right_format_date():
    right_format_date_message = QMessageBox()
    font = QtGui.QFont()
    font.setPointSize(18)
    right_format_date_message.setFont(font)
    right_format_date_message.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                            "color: rgb(186, 186, 186);")
    right_format_date_message.setWindowTitle("Ошибка!")
    right_format_date_message.setText("Дату рождения необходимо вводить в формате: гггг-мм-дд, "
                                      "где гггг - год рождения, мм - месяц рождения, дд - день рождения.")
    right_format_date_message.setIcon(QMessageBox.Warning)
    right_format_date_message.setStandardButtons(QMessageBox.Ok)
    right_format_date_message.exec_()


def edit_data_page():
    if MainWindow.tableWidget_1.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_1.currentRow()
        column = MainWindow.tableWidget_1.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_1.item(row, column+1).text(),
                                              MainWindow.tableWidget_1.item(row, column+2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_1.item(row, column-1).text(),
                                              MainWindow.tableWidget_1.item(row, column+1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_1.item(row, column-2).text(),
                                              MainWindow.tableWidget_1.item(row, column-1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_2.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_2.currentRow()
        column = MainWindow.tableWidget_2.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_2.item(row, column + 1).text(),
                                              MainWindow.tableWidget_2.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_2.item(row, column - 1).text(),
                                              MainWindow.tableWidget_2.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_2.item(row, column - 2).text(),
                                              MainWindow.tableWidget_2.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_3.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_3.currentRow()
        column = MainWindow.tableWidget_3.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_3.item(row, column + 1).text(),
                                              MainWindow.tableWidget_3.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_3.item(row, column - 1).text(),
                                              MainWindow.tableWidget_3.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_3.item(row, column - 2).text(),
                                              MainWindow.tableWidget_3.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_4.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_4.currentRow()
        column = MainWindow.tableWidget_4.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_4.item(row, column + 1).text(),
                                              MainWindow.tableWidget_4.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_4.item(row, column - 1).text(),
                                              MainWindow.tableWidget_4.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_4.item(row, column - 2).text(),
                                              MainWindow.tableWidget_4.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_5.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_5.currentRow()
        column = MainWindow.tableWidget_5.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_5.item(row, column + 1).text(),
                                              MainWindow.tableWidget_5.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_5.item(row, column - 1).text(),
                                              MainWindow.tableWidget_5.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_5.item(row, column - 2).text(),
                                              MainWindow.tableWidget_5.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_6.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_6.currentRow()
        column = MainWindow.tableWidget_6.currentColumn()
        if column == 0:
            print(len(EditWindow.edit_input.text()))
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_6.item(row, column + 1).text(),
                                              MainWindow.tableWidget_6.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_6.item(row, column - 1).text(),
                                              MainWindow.tableWidget_6.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_6.item(row, column - 2).text(),
                                              MainWindow.tableWidget_6.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_7.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_7.currentRow()
        column = MainWindow.tableWidget_7.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_7.item(row, column+1).text(),
                                              MainWindow.tableWidget_7.item(row, column+2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_7.item(row, column-1).text(),
                                              MainWindow.tableWidget_7.item(row, column+1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_7.item(row, column-2).text(),
                                              MainWindow.tableWidget_7.item(row, column-1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_8.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_8.currentRow()
        column = MainWindow.tableWidget_8.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_8.item(row, column + 1).text(),
                                              MainWindow.tableWidget_8.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_8.item(row, column - 1).text(),
                                              MainWindow.tableWidget_8.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_8.item(row, column - 2).text(),
                                              MainWindow.tableWidget_8.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_9.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_9.currentRow()
        column = MainWindow.tableWidget_9.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_9.item(row, column + 1).text(),
                                              MainWindow.tableWidget_9.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_9.item(row, column - 1).text(),
                                              MainWindow.tableWidget_9.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_9.item(row, column - 2).text(),
                                              MainWindow.tableWidget_9.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_10.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_10.currentRow()
        column = MainWindow.tableWidget_10.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_10.item(row, column + 1).text(),
                                              MainWindow.tableWidget_10.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_10.item(row, column - 1).text(),
                                              MainWindow.tableWidget_10.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_10.item(row, column - 2).text(),
                                              MainWindow.tableWidget_10.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_11.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_11.currentRow()
        column = MainWindow.tableWidget_11.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_11.item(row, column + 1).text(),
                                              MainWindow.tableWidget_11.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_11.item(row, column - 1).text(),
                                              MainWindow.tableWidget_11.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_11.item(row, column - 2).text(),
                                              MainWindow.tableWidget_11.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_12.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_12.currentRow()
        column = MainWindow.tableWidget_12.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_12.item(row, column + 1).text(),
                                              MainWindow.tableWidget_12.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_12.item(row, column - 1).text(),
                                              MainWindow.tableWidget_12.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_12.item(row, column - 2).text(),
                                              MainWindow.tableWidget_12.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    if MainWindow.tableWidget_13.cellClicked.connect(open_edit_data_window):
        cursor = connection.cursor()
        row = MainWindow.tableWidget_13.currentRow()
        column = MainWindow.tableWidget_13.currentColumn()
        if column == 0:
            if len(EditWindow.edit_input.text()) < 2:
                few_characters()
            else:
                insert_query = "Update contacts set fullname = %s where telephone_number = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_13.item(row, column + 1).text(),
                                              MainWindow.tableWidget_13.item(row, column + 2).text()))
                successful_editing()
                connection.commit()
        if column == 1:
            if len(EditWindow.edit_input.text()) < 6:
                few_characters()
            else:
                insert_query = "Update contacts set telephone_number = %s where fullname = %s and dob = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_13.item(row, column - 1).text(),
                                              MainWindow.tableWidget_13.item(row, column + 1).text()))
                successful_editing()
                connection.commit()
        if column == 2:
            try:
                insert_query = "Update contacts set dob = %s where fullname = %s and telephone_number = %s"
                cursor.execute(insert_query, (EditWindow.edit_input.text(),
                                              MainWindow.tableWidget_13.item(row, column - 2).text(),
                                              MainWindow.tableWidget_13.item(row, column - 1).text()))
                successful_editing()
                connection.commit()
            except:
                right_format_date()
    EditWindow.close()


def notification():
    notification_query = "SELECT fullname,DAY(dob) FROM contacts WHERE DAY(dob) BETWEEN DAY(CURRENT_DATE)+1 " \
                         "AND DAY(CURRENT_DATE)+7"
    cursor.execute(notification_query)
    result_notification_query = cursor.fetchall()
    if result_notification_query is None:
        pass
    else:
        list_of_dob = []
        for i in result_notification_query:
            list_of_dob.append(str(i["fullname"]) + " - " + str(i["DAY(dob)"]) + "-го числа.")
            summary_line = "\n".join(list_of_dob)
            notification_message = QMessageBox()
            font = QtGui.QFont()
            font.setPointSize(18)
            notification_message.setFont(font)
            notification_message.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                               "color: rgb(186, 186, 186);")
            notification_message.setWindowTitle("Напоминание:")
            notification_message.setText("Список именинников на ближайшую неделю:" "\n" + "" +
                                         "\n" + summary_line + "\n" + "" + "\n" + "Не забудьте поздравить их!!!")
            notification_message.setStandardButtons(QMessageBox.Ok)
            notification_message.exec_()


def actions():
    LoginWindow.registration_btn.clicked.connect(open_registration_window)
    LoginWindow.label_forgot_pass.clicked.connect(open_restore_window)
    LoginWindow.login_btn.clicked.connect(log_in)
    LoginWindow.cancel_btn.clicked.connect(clear_login_fields)
    RegistrationWindow.sign_up_btn.clicked.connect(registration)
    MainWindow.refresh_btn.clicked.connect(refresh)
    MainWindow.exit_btn.clicked.connect(log_out)
    MainWindow.New_btn.clicked.connect(open_new_contact_window)
    NewContactWindow.add_btn.clicked.connect(add_new_contact)
    MainWindow.tableWidget_1.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_2.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_3.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_4.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_5.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_6.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_7.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_8.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_9.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_10.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_11.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_12.cellClicked.connect(open_edit_data_window)
    MainWindow.tableWidget_13.cellClicked.connect(open_edit_data_window)
    EditWindow.edit_btn.clicked.connect(edit_data_page)
    EditWindow.delete_btn.clicked.connect(delete_contact)
    MainWindow.pushButton_1.clicked.connect(changed_to_1page)
    MainWindow.pushButton_2.clicked.connect(changed_to_2page)
    MainWindow.pushButton_3.clicked.connect(changed_to_3page)
    MainWindow.pushButton_4.clicked.connect(changed_to_4page)
    MainWindow.pushButton_5.clicked.connect(changed_to_5page)
    MainWindow.pushButton_6.clicked.connect(changed_to_6page)
    MainWindow.pushButton_7.clicked.connect(changed_to_7page)
    MainWindow.pushButton_8.clicked.connect(changed_to_8page)
    MainWindow.pushButton_9.clicked.connect(changed_to_9page)
    MainWindow.pushButton_10.clicked.connect(changed_to_10page)
    MainWindow.pushButton_11.clicked.connect(changed_to_11page)
    MainWindow.pushButton_12.clicked.connect(changed_to_12page)
    MainWindow.pushButton_13.clicked.connect(changed_to_13page)


# Запуск всех окон
app = QtWidgets.QApplication(sys.argv)
LoginWindow = LoginWindow()
RegistrationWindow = RegistrationWindow()
RestoreWindow = RestoreWindow()
MainWindow = MainWindow()
NewContactWindow = NewContactWindow()
EditWindow = EditWindow()
actions()


# Первый коннект к бд. Создание таблиц: users(пользователи программы) и contacts(контакты).
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


# Чек на пустую бд, запуск программы.
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
    if result_autologin_query is None:
        LoginWindow.show()
    else:
        MainWindow.label_user.setText(result_autologin_query["name"])
        notification()
        refresh()
        MainWindow.show()


sys.exit(app.exec_())
