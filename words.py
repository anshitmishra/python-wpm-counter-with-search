import imp
from operator import indexOf
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QLabel, QLineEdit
from PyQt5 import uic
from PyQt5 import QtGui
import sys
import time


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("word.ui", self)
        self.setWindowTitle("Word Counte And search ")
        self.setWindowIcon(QtGui.QIcon('image/logo.svg'))
        # tagging elements
        self.EditData = self.findChild(QTextEdit, "textEdit")
        self.readData = self.findChild(QTextEdit, "textEdit_2")
        self.start = self.findChild(QPushButton, "pushButton_2")
        self.searchButton = self.findChild(QPushButton, "pushButton")
        self.timeMin = self.findChild(QLabel, "label_4")
        self.statusReport = self.findChild(QLabel, "label_3")
        self.searchInput = self.findChild(QLineEdit, "lineEdit")

        # adding events
        self.EditData.setReadOnly(True)
        self.start.clicked.connect(lambda: self.startGame())
        self.searchButton.clicked.connect(lambda: self.searchData())
        self.EditData.textChanged.connect(lambda: self.do())

        # variables
        self.startTime = 0
        self.endTime = 0

        # show app
        self.show()

    def startGame(self):
        self.EditData.setReadOnly(False)
        self.start.setEnabled(False)
        self.startTime = int(time.time())

    def do(self):
        self.readTextLen = self.readData.toPlainText()
        self.readTextLen = len(self.readTextLen.split(" "))

        self.currReadTextLen = self.EditData.toPlainText()
        self.currReadTextLen = len(self.currReadTextLen.split(" "))

        if(self.currReadTextLen == self.readTextLen):
            self.EditData.setReadOnly(True)
            self.start.setEnabled(True)
            self.endTime = int(time.time())
            self.win()

    def win(self):
        totalTime = self.endTime - self.startTime
        ss = totalTime
        mm = 0
        if(ss == 60):
            mm = mm+1
            ss = 00
        
        data = str(str(mm)+":"+str(ss))
        self.timeMin.setText(str(data))
        word = int((self.currReadTextLen / 5) / (totalTime / 60))
        self.statusReport.setText(f'{str(word)} word per min ')

    def searchData(self):
        self.readText = self.readData.toPlainText()
        self.readText = self.readText.split(" ")
        searchValue = self.searchInput.text()
        textCounter = 0
        text = ""
        for x in self.readText:
            if x == searchValue:
                self.readText[textCounter] = '<b style="background:yellow;">'+x+'</b>'
            text += " "+self.readText[textCounter]+" "
            textCounter += 1
        x = str(text)
        self.readData.setHtml(x)


        

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
