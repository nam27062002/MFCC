from PyQt5 import QtGui, QtWidgets, QtCore
import sys, os
import UIStart,UIStatistical
import Training,Statistical,ShowSignal
from ShowEigenvectors import Process as showVector
class UI:
    def __init__(self):
        self.ui = ""
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.URL = ""
        self.training = [Training.Process(13),Training.Process(26),Training.Process(39)]
        self.statisticals = [Statistical.statistical(self.training[0]),Statistical.statistical(self.training[1]),Statistical.statistical(self.training[2])]
    def __UIStart(self):
        self.ui = UIStart.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui.frame.setAcceptDrops(True)
        self.ui.frame.dragEnterEvent = self.DragEnter
        self.ui.frame.dropEvent = self.dropEvent
        self.ui.pushButton.clicked.connect(self.showVector)
        self.ui.pushButton_2.clicked.connect(self.__UIStatistical)
        self.ui.frame.mousePressEvent = self.openFolder
    def openFolder(self,e):
        directory = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.wav)")
        if directory[0] != "":
            self.showASignal(directory[0])
    def __UIStatistical(self):
        self.ui = UIStatistical.Ui_MainWindow()
        arrPercent = [round(self.statisticals[0].Percent,2),round(self.statisticals[1].Percent,2),round(self.statisticals[2].Percent,2)]
        self.ui.setupUi(self.MainWindow,arrPercent,self.statisticals[0].ARR)
        self.ui.pushButton.clicked.connect(self.__UIStart)
        self.MainWindow.show()
    def showVector(self):
        showVector(self.training[0].getEigenvectors()).show()
    def DragEnter(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "wav":
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "wav":
            event.accept()
            self.showASignal(x)
        else:
            event.ignore()
    def showASignal(self,url):
        ShowSignal.Process(url,self.training[0].compare(url)[1]).show()
    def loop(self):
        self.__UIStart()
        sys.exit(self.app.exec_())
