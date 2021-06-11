from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class EditWindow(QMainWindow):
    def __init__(self):
        super(EditWindow, self).__init__()
        self.setObjectName("EditWindow")
        self.setFixedSize(500, 300)
        self.setStyleSheet("background-color: rgb(42, 42, 42);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_edit = QtWidgets.QLabel(self.centralwidget)
        self.label_edit.setGeometry(QtCore.QRect(25, 35, 450, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_edit.setFont(font)
        self.label_edit.setStyleSheet("background-color: rgb(150, 150, 150);\n"
                                      "color: rgb(50, 50, 50);")
        self.label_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_edit.setObjectName("label_edit")
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(30, 230, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                    "color: rgb(186, 186, 186);")
        self.edit_btn.setObjectName("edit_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(280, 230, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                      "color: rgb(186, 186, 186);")
        self.delete_btn.setObjectName("delete_btn")
        self.edit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_input.setGeometry(QtCore.QRect(65, 120, 370, 50))
        self.edit_input.setStyleSheet("background-color: rgb(83, 83, 83);\n"
                                      "color: rgb(186, 186, 186);")
        self.edit_input.setObjectName("edit_input")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, EditWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("EditWindow", "Удаление и редактирование данных:"))
        self.label_edit.setText(_translate("EditWindow", "Удаление и редактирование данных:"))
        self.edit_btn.setText(_translate("EditWindow", "Редактировать"))
        self.delete_btn.setText(_translate("EditWindow", "Удалить"))
        self.edit_input.setPlaceholderText(_translate("EditWindow", "Изменить значение на..."))
