#!/usr/bin/env python3.8

import requests
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from modal import Ui_MainWindow
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

url = 'https://pastebin.com/api/api_post.php'

def buttonClicked(self):
    sendRequest(confirmData())
    ui.lineEdit.clear()
    

def confirmData():
    text = ui.textEdit.toPlainText()
    name = ui.lineEdit.text()
    user_data = {
        'api_dev_key': '',
        'api_option': 'paste',
        'api_paste_code': text,
        'api_paste_name': name,
        'api_paste_expire_date': 'N',
        'api_results_limit': '100'
    }

    return user_data

def sendRequest(user_data):
    r = requests.post(url, data= user_data)

    if r.status_code == 200:
        ui.textBrowser.setText(r.text)
    else:
        ui.textBrowser.setText("Error")


ui.pushButton.clicked.connect(buttonClicked)
sys.exit(app.exec_())
