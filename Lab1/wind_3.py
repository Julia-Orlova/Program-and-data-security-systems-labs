from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QMessageBox, QLineEdit
import os
from lab1 import main_wind


class Window3(QMainWindow):
    def __init__(self):
        super(Window3, self).__init__()
        self.setGeometry(300, 200, 600, 500)
        self.setWindowTitle("Ви увійшли як користувач")

        self.label_3 = QLabel(self)
        self.label_3.setText("Користувач має права на\nчитання і виконання (r-x)")
        self.label_3.setFont(QtGui.QFont("Times", 12))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 400, 50))
        self.label_3.move(100, 30)

        self.label_pwd = QLabel(self)
        self.label_pwd.setText("pwd")
        self.label_pwd.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.label_pwd.move(30, 110)

        self.line_pwd = QLineEdit(self)
        self.line_pwd.setGeometry(QtCore.QRect(0, 0, 430, 30))
        self.line_pwd.move(70, 110)

        self.button_pwd = QPushButton(self)
        self.button_pwd.setText("pwd")
        self.button_pwd.setFont(QtGui.QFont("Times", 12))
        self.button_pwd.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.button_pwd.move(510, 110)
        self.button_pwd.clicked.connect(self.pwd)

        self.label_ls = QLabel(self)
        self.label_ls.setText("ls")
        self.label_ls.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.label_ls.move(30, 150)

        self.line_ls = QLineEdit(self)
        self.line_ls.setGeometry(QtCore.QRect(0, 0, 430, 30))
        self.line_ls.move(70, 150)

        self.button_ls = QPushButton(self)
        self.button_ls.setText("ls")
        self.button_ls.setFont(QtGui.QFont("Times", 12))
        self.button_ls.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.button_ls.move(510, 150)
        self.button_ls.clicked.connect(self.ls)

        self.label_cd = QLabel(self)
        self.label_cd.setText("cd")
        self.label_cd.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.label_cd.move(30, 190)

        self.line_cd = QLineEdit(self)
        self.line_cd.setGeometry(QtCore.QRect(0, 0, 430, 30))
        self.line_cd.move(70, 190)

        self.button_cd = QPushButton(self)
        self.button_cd.setText("cd")
        self.button_cd.setFont(QtGui.QFont("Times", 12))
        self.button_cd.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.button_cd.move(510, 190)
        self.button_cd.clicked.connect(self.cd)

        self.label_mkdir = QLabel(self)
        self.label_mkdir.setText("mkdir")
        self.label_mkdir.setGeometry(QtCore.QRect(0, 0, 40, 30))
        self.label_mkdir.move(20, 230)

        self.line_mkdir = QLineEdit(self)
        self.line_mkdir.setGeometry(QtCore.QRect(0, 0, 430, 30))
        self.line_mkdir.move(70, 230)

        self.button_mkdir = QPushButton(self)
        self.button_mkdir.setText("mkdir")
        self.button_mkdir.setFont(QtGui.QFont("Times", 12))
        self.button_mkdir.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.button_mkdir.move(510, 230)
        self.button_mkdir.clicked.connect(self.mkdir)

        self.label_vi = QLabel(self)
        self.label_vi.setText("vi")
        self.label_vi.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.label_vi.move(30, 270)

        self.line_vi = QLineEdit(self)
        self.line_vi.setGeometry(QtCore.QRect(0, 0, 430, 30))
        self.line_vi.move(70, 270)

        self.button_vi = QPushButton(self)
        self.button_vi.setText("vi")
        self.button_vi.setFont(QtGui.QFont("Times", 12))
        self.button_vi.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.button_vi.move(510, 270)
        self.button_vi.clicked.connect(self.vi)

        self.label_rm = QLabel(self)
        self.label_rm.setText("rm")
        self.label_rm.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.label_rm.move(30, 310)

        self.line_rm = QLineEdit(self)
        self.line_rm.setGeometry(QtCore.QRect(0, 0, 430, 30))
        self.line_rm.move(70, 310)

        self.button_rm = QPushButton(self)
        self.button_rm.setText("rm")
        self.button_rm.setFont(QtGui.QFont("Times", 12))
        self.button_rm.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.button_rm.move(510, 310)
        self.button_rm.clicked.connect(self.rm)

        self.label_3 = QLabel(self)
        self.label_3.setFont(QtGui.QFont("Times", 8))
        self.label_3.setGeometry(QtCore.QRect(0, 0, 560, 120))
        self.label_3.move(20, 360)

    def input_values(self):
        self.pwd_received = self.line_pwd.text()
        self.ls_received = self.line_ls.text()
        self.cd_received = self.line_cd.text()
        self.mkdir_received = self.line_mkdir.text()
        self.vi_received = self.line_vi.text()
        self.rm_received = self.line_rm.text()

    def pwd(self):
        path = os.getcwd()
        self.label_3.setText(path)

    def ls(self):
        a = []
        path = os.getcwd()
        for filename in os.listdir(path):
            a.append(filename)
        self.label_3.setText(str(a))

    def cd(self):
        try:
            self.input_values()
            os.chdir(self.cd_received)
        except:
            self.error("Введіть, будь ласка, шлях до потрібної папки!")

    def mkdir(self):
        self.error("Ви не маєте прав доступу для даної команди!\nУвійдіть як адміністратор.")

    def vi(self):
        self.error("Ви не маєте прав доступу для даної команди!\nУвійдіть як адміністратор.")

    def rm(self):
        self.error("Ви не маєте прав доступу для даної команди!\nУвійдіть як адміністратор.")

    def error(self, message):
        self.invalid_input_msg = QMessageBox(self)
        self.invalid_input_msg.setWindowTitle("Error")
        self.invalid_input_msg.setText(message)
        self.invalid_input_msg.setIcon(QMessageBox.Warning)
        self.invalid_input_msgbox = self.invalid_input_msg.exec_()