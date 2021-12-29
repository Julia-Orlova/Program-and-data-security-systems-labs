from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QInputDialog, QMessageBox
import sys, time, random, math
from lab2 import virtual_wind
from lab2 import wind_2, wind_3


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(300, 200, 340, 180)
        self.setWindowTitle("Лабораторна робота №1")

        self.cap_label = QLabel(self)
        self.cap_label.setText("Оберіть групу користувачів:")
        self.cap_label.setFont(QtGui.QFont("Times", 14))
        self.cap_label.setGeometry(QtCore.QRect(0, 0, 300, 50))
        self.cap_label.move(30, 20)

        self.button_call_2 = QPushButton(self)
        self.button_call_2.setText("Адміністратор")
        self.button_call_2.setFont(QtGui.QFont("Times", 11))
        self.button_call_2.setGeometry(QtCore.QRect(0, 0, 140, 60))
        self.button_call_2.move(20, 80)
        self.button_call_2.clicked.connect(self.call_wind2)

        self.button_call_3 = QPushButton(self)
        self.button_call_3.setText("Користувач")
        self.button_call_3.setFont(QtGui.QFont("Times", 11))
        self.button_call_3.setGeometry(QtCore.QRect(0, 0, 140, 60))
        self.button_call_3.move(180, 80)
        self.button_call_3.clicked.connect(self.call_wind3)

    def call_wind2(self):
        self.get_a1, self.if_get_a1_in = QInputDialog.getText(self, "Пароль", "Введіть пароль адміністратора:")
        if self.get_a1 == '1111':
            self.wind2 = wind_2.Window2()
            self.wind2.show()
        else:
            self.error("Ви ввели неправильний пароль.\nСпробуйте ще раз або увійдіть як користувач.")


    def call_wind3(self):
        self.get_a2, self.if_get_a2_in = QInputDialog.getText(self, "ChooseUser", "Ви новий користувач? (так - 1, ні - 0):")
        if self.get_a2 == '1':
            file = open('logbook.txt')
            self.input_name()
            file.writelines(self.get_a4)
            index = str(self.self.get_a4).find(',')
            right_pass = self.right_password(str(self.self.get_a4)[index:])
            while right_pass == False:
                self.input_name()
            self.wind3 = wind_3.Window3()
            self.wind3.show()
            while True:
                start = time.perf_counter()
                end = time.perf_counter()
                a, x = random.randint(0, 1000), random.randint(0, 1000)
                while (end - start) < 180:
                    end = time.perf_counter()
                self.get_a5, self.if_get_a5_in = QInputDialog.getText(self, "Question",
                                              "Розрахуйте секретну фенкцію. Вхідні дані: {0}, {1}".format(a, x))
                count = 0
                while self.get_a4 != math.lg(a + x):
                    self.error("В доступі відмовлено.")
                    count += 10
                    if count == 10:
                        file = open('logbook.txt', 'r')
                        logbook = file.readlines()
                        logbook.remove(self.get_a4)
                        break

        elif self.get_a2 == '0':
            self.input_name()
            file = open('logbook.txt')
            logbook = file.readlines()
            for i in range(len(logbook)):
                if logbook[i] == self.get_a4:
                    self.wind3 = wind_3.Window3()
                    self.wind3.show()
                    while True:
                        start = time.perf_counter()
                        end = time.perf_counter()
                        a, x = random.randint(0, 1000), random.randint(0, 1000)
                        while (end - start) < 180:
                            end = time.perf_counter()
                        self.get_a6, self.if_get_a6_in = QInputDialog.getText(self, "Question",
                                              "Розрахуйте секретну фенкцію. Вхідні дані: {0}, {1}".format(a, x))
                        count = 0
                        while self.get_a4 != math.lg(a + x):
                            self.error("В доступі відмовлено.")
                            count += 10
                            if count == 10:
                                file = open('logbook.txt', 'r')
                                logbook = file.readlines()
                                logbook.remove(self.get_a4)
                                break
        else:
            self.error("Потрібно ввести 1 або 0!")

    def input_name(self):
        self.get_a4, self.if_get_a4_in = QInputDialog.getText(self, "Username",
                                                              "Введіть ваше ім'я і пароль через кому:")

    def right_password(self, password):
        if len(password) < 4:
            self.error("Довжина паролю повинна бути >= 4!")
            return False

    def error(self, message):
        self.invalid_input_msg = QMessageBox(self)
        self.invalid_input_msg.setWindowTitle("Error")
        self.invalid_input_msg.setText(message)
        self.invalid_input_msg.setIcon(QMessageBox.Warning)
        self.invalid_input_msgbox = self.invalid_input_msg.exec_()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
