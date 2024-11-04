# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BOOTY.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
import os
import serial
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1437, 890)
        MainWindow.setStyleSheet("background-color: rgb(226, 227, 255);")

        # Central widget setup
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Frame for title and subtitle
        self.setup_title_frame()

        # Control Board setup
        self.Control_Board = QtWidgets.QFrame(self.centralwidget)
        self.Control_Board.setGeometry(QtCore.QRect(0, 160, 451, 691))
        self.Control_Board.setStyleSheet("background-color: rgb(29, 114, 128);")
        self.Control_Board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Control_Board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Control_Board.setObjectName("Control_Board")
        self.setup_control_board()

        # Main Graph Frame setup
        self.setup_graph_frame(MainWindow)

        # Finalize UI setup
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setup_title_frame(self):
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1431, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.TITLE = QtWidgets.QLabel(self.frame)
        self.TITLE.setGeometry(QtCore.QRect(20, 0, 1411, 151))
        self.TITLE.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                 "font: 75 8pt \"Trebuchet MS\";\n"
                                 "background-color: rgb(17, 99, 116);\n"
                                 "border-color: rgb(0, 0, 0);\n"
                                 "gridline-color: rgb(0, 0, 0);")
        self.TITLE.setObjectName("TITLE")

        self.Team_photo = QtWidgets.QLabel(self.frame)
        self.Team_photo.setGeometry(QtCore.QRect(1170, -70, 331, 291))
        self.Team_photo.setMinimumSize(QtCore.QSize(181, 0))
        self.Team_photo.setStyleSheet("image: url(:/newPrefix/Pictures/poop.png);\n"
                                       "background-color: rgb(17, 99, 116);")
        self.Team_photo.setText("")
        self.Team_photo.setObjectName("Team_photo")

        self.Sub_Title = QtWidgets.QLabel(self.frame)
        self.Sub_Title.setGeometry(QtCore.QRect(570, 0, 351, 151))
        self.Sub_Title.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                      "font: 75 8pt \"Trebuchet MS\";\n"
                                      "background-color: rgb(17, 99, 116);\n"
                                      "border-color: rgb(0, 0, 0);\n"
                                      "gridline-color: rgb(0, 0, 0);")
        self.Sub_Title.setObjectName("Sub_Title")

    def setup_control_board(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Control_Board)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Control frame setup
        self.frame_11 = QtWidgets.QFrame(self.Control_Board)
        self.frame_11.setStyleSheet("background-color: rgb(17, 99, 116);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.setup_control_frame()

        self.verticalLayout.addWidget(self.frame_11)

    def setup_control_frame(self):
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame_5 = QtWidgets.QFrame(self.frame_11)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.setup_control_buttons()

        self.verticalLayout_2.addWidget(self.frame_5)

    def setup_control_buttons(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setStyleSheet("background-color: rgb(17, 99, 116);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.setup_buttons_in_frame(self.gridLayout_3)

        self.horizontalLayout.addWidget(self.frame_10)

        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setStyleSheet("background-color: rgb(17, 99, 116);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.setup_additional_buttons()

        self.horizontalLayout.addWidget(self.frame_12)

    def setup_buttons_in_frame(self, gridLayout):
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        gridLayout.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.frame_10)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

    def setup_additional_buttons(self):
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 140, 161, 23))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 190, 161, 23))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 250, 161, 23))
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_10.setGeometry(QtCore.QRect(10, 250, 161, 23))
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")

        self.label_5 = QtWidgets.QLabel(self.frame_12)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 171, 21))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 171, 21))
        self.label_6.setObjectName("label_6")

        self.pushButton_6 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 90, 161, 23))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 40, 161, 23))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")

    def setup_graph_frame(self, MainWindow):
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(450, 160, 981, 691))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout_3.addWidget(self.canvas)

        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frame.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>poop</p></body></html>"))
        self.TITLE.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>poop</p><p><br/></p></body></html>"))
        self.TITLE.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:400; color:#ffffff;\">SEA TEAM 1</span></p></body></html>"))
        self.Sub_Title.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>poop</p><p><br/></p></body></html>"))
        self.Sub_Title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:400; color:#ffffff;\">B.O.A.T.</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Ping Plane"))
        self.pushButton_4.setText(_translate("MainWindow", "Calibrate Altituide"))
        self.pushButton_2.setText(_translate("MainWindow", "Calibrate Gyroscope"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "Calibratie airspeed"))
        self.pushButton_8.setText(_translate("MainWindow", "Set COM channel"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.label_5.setText(_translate("MainWindow", "Time: 00:00:00"))
        self.label_6.setText(_translate("MainWindow", "Status: NULL"))

# Additional methods for the functionalities can be added below
# Example: Methods to handle button clicks and plot graphs

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
