from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class NewContactWindow(QMainWindow):
    def __init__(self):
        super(NewContactWindow, self).__init__()
        self.setObjectName("NewContactWindow")
        self.setFixedSize(560, 440)
        self.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_new_contact = QtWidgets.QLabel(self.centralwidget)
        self.label_new_contact.setGeometry(QtCore.QRect(130, 30, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_new_contact.setFont(font)
        self.label_new_contact.setStyleSheet("background-color: rgb(150, 150, 150);\n"
                                             "color: rgb(50, 50, 50);")
        self.label_new_contact.setAlignment(QtCore.Qt.AlignCenter)
        self.label_new_contact.setObjectName("label_new_contact")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(70, 320, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                   "color: rgb(186, 186, 186);")
        self.add_btn.setObjectName("add_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(310, 320, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                      "color: rgb(186, 186, 186);")
        self.cancel_btn.setObjectName("cancel_btn")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(80, 100, 400, 40))
        self.name_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                      "color: rgb(186, 186, 186);")
        self.name_input.setObjectName("name_input")
        self.telephone_number_input = QtWidgets.QLineEdit(self.centralwidget)
        self.telephone_number_input.setGeometry(QtCore.QRect(80, 170, 400, 40))
        self.telephone_number_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                                  "color: rgb(186, 186, 186);")
        self.telephone_number_input.setObjectName("telephone_number_input")
        self.dob_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dob_dateEdit.setCalendarPopup(True)
        self.dob_dateEdit.setGeometry(QtCore.QRect(320, 240, 110, 40))
        self.dob_dateEdit.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                        "color: rgb(186, 186, 186);")
        self.dob_dateEdit.setObjectName("dob_dateEdit")
        self.dob_label = QtWidgets.QLabel(self.centralwidget)
        self.dob_label.setGeometry(QtCore.QRect(130, 240, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dob_label.setFont(font)
        self.dob_label.setStyleSheet("background-color: rgb(150, 150, 150);\n"
                                     "color: rgb(50, 50, 50);")
        self.dob_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dob_label.setObjectName("dob_label")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, NewContactWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("NewContactWindow", "Добавление контакта"))
        self.label_new_contact.setText(_translate("NewContactWindow", "Добавить новый контакт"))
        self.add_btn.setText(_translate("NewContactWindow", "Добавить"))
        self.cancel_btn.setText(_translate("NewContactWindow", "Отмена"))
        self.name_input.setPlaceholderText(_translate("NewContactWindow", "Имя..."))
        self.telephone_number_input.setPlaceholderText(_translate("NewContactWindow", "Номер телефона..."))
        self.dob_label.setText(_translate("NewContactWindow", "Дата рождения:"))
