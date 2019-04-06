
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyperclip
import sys
import csv
import time
from threading import *


get_text = pyperclip.paste()
random_text = get_text


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(539, 363)
        MainWindow.setWindowIcon(QtGui.QIcon('mainlogo.ico'))
        # MainWindow.setStyleSheet("background-color:white;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 391, 311))
        self.listWidget.setObjectName("listWidget")

        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(430, 50, 75, 23))
        # self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 80, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_2.setStyleSheet("background-color:red")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 110, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("width: 50%")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 290, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 20, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_5.clicked.connect(self.copy_button)
        self.pushButton_2.clicked.connect(self.delete_selected)
        self.pushButton_3.clicked.connect(self.delete_all_button)
        self.pushButton_4.clicked.connect(self.about_button)

        # error_dialog = QtWidgets.QErrorMessage()
        # error_dialog.showMessage('Oh no!')

    def enable_disable_copy_delete_button(self):
        try:
            self.listWidget.selectedItems()[0]
            self.pushButton_5.setDisabled(False)
            self.pushButton_2.setDisabled(False)
        except IndexError:
            self.pushButton_5.setDisabled(True)
            self.pushButton_2.setDisabled(True)

    def copy_button(self):
        try:
            item = self.listWidget.selectedItems()[0].text()
            # count = self.listWidget.count()
            # for i in count:
            #     if self.listWidget.item(i).text() == item:
            #         break
            pyperclip.copy(item)
        except IndexError:
            print('select an item')
        except Exception:
            print('an error occurred')

        # print(self.listWidget.item(0).text())

        
    def add_from_csv_to_listWidget(self):
        self.listWidget.clear()
        with open('data.csv', 'r') as csvFile:
            obj_reader = csv.reader(csvFile)
            for row in obj_reader:
                try:
                    self.listWidget.addItem(str(row[0]))
                except Exception:
                    pass

    def add_to_csv(self, data):

        # count = self.listWidget.count()
        # for i in range(count):
        #     if self.listWidget.item(i).text() == data:
        #         return
        # print('test')

        try:
            if data == self.listWidget.selectedItems()[0].text():
                return
        except Exception:
            pass

        with open('data.csv', 'a', newline='') as csvFile:
            obj_writer = csv.writer(csvFile)
            obj_writer.writerow([data])
        self.add_from_csv_to_listWidget()

    def delete_selected(self):
        with open('data.csv', 'r') as csvFile:
            reader = csv.reader(csvFile)
            content_of_data = []
            for row in reader:
                try:
                    content_of_data.append(row[0])
                except Exception:
                    pass

        if self.listWidget.selectedItems()[0].text() in content_of_data:
            content_of_data.remove(self.listWidget.selectedItems()[0].text())

            with open('data.csv', 'w', newline='') as csvFile:
                writer = csv.writer(csvFile)
                for e in content_of_data:
                    writer.writerow([e])

            self.add_from_csv_to_listWidget()

    def delete_all(self):
        with open('data.csv', 'w', newline='') as csvFile:
            pass

        self.add_from_csv_to_listWidget()

    def delete_all_button(self):
        self.message_box()

    def message_box(self):
        self.alert_box = QtWidgets.QMessageBox()
        self.alert_box.setWindowIcon(QtGui.QIcon('alert.ico'))
        self.alert_box.setWindowTitle('Delete All')
        self.alert_box.setText("Are you sure?")
        self.alert_box.addButton(QtWidgets.QMessageBox.Yes).clicked.connect(self.delete_all)
        self.alert_box.addButton(QtWidgets.QMessageBox.No)
        self.alert_box.exec_()

    def about_button(self):
        self.messagebox_about = QtWidgets.QMessageBox()
        self.messagebox_about.setWindowIcon(QtGui.QIcon('mainlogo.ico'))
        self.messagebox_about.setText('MultiClipBoard \t\nDeveloped by : Abhishek Kumar \t\nVersion : 19.2\t')
        self.messagebox_about.setWindowTitle('About')
        self.messagebox_about.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MultiClipBoard"))
        # self.pushButton.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete All"))
        self.pushButton_4.setText(_translate("MainWindow", "About"))
        self.pushButton_5.setText(_translate("MainWindow", "Copy"))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UiMainWindow()
ui.setupUi(MainWindow)
ui.add_from_csv_to_listWidget()


def write_data_to_csv_and_update_widget():
    while True:
        ui.enable_disable_copy_delete_button()
        global get_text, random_text
        get_text = pyperclip.paste()
        if get_text != random_text:
            ui.add_to_csv(get_text)
            random_text = get_text
        time.sleep(0.1)


th1 = Thread(target=write_data_to_csv_and_update_widget)
th1.setDaemon(True)
th1.start()

MainWindow.show()
sys.exit(app.exec_())
