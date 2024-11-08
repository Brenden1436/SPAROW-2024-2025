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

        # sets up Title, Sub-title, and Team photo for the title frame
        self.setup_title_frame()

        # the control board consisting of buttons and text labels to interact with the aircraft
        self.setup_control_board()

        # sets up the graphs that will display telemtry from the aircraft
        self.setup_graphs()

        # makes the text appear on the ui
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # sets up WHAT each button does
        self.button_functions()

        



    def setup_title_frame(self):

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1431, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Main title that says SEA TEAM 1
        self.TITLE = QtWidgets.QLabel(self.frame)
        self.TITLE.setGeometry(QtCore.QRect(20, 0, 1411, 151))
        self.TITLE.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                 "font: 75 8pt \"Trebuchet MS\";\n"
                                 "background-color: rgb(154, 131, 175);\n"
                                 "border-color: rgb(0, 0, 0);\n"
                                 "gridline-color: rgb(0, 0, 0);")
        self.TITLE.setObjectName("TITLE")

        # the setup of the Team photo
        self.Team_photo = QtWidgets.QLabel(self.frame)
        self.Team_photo.setGeometry(QtCore.QRect(1170, -70, 331, 291))
        self.Team_photo.setMinimumSize(QtCore.QSize(181, 0))
        self.Team_photo.setStyleSheet("image: url(:/newPrefix/Pictures/poop.png);\n"
                                      "background-color: rgb(154, 131, 175);")
        self.Team_photo.setText("")
        self.Team_photo.setObjectName("Team_photo")

        # A sub title that says the name of our aircraft: B.O.A.T.
        self.Sub_Title = QtWidgets.QLabel(self.frame)
        self.Sub_Title.setGeometry(QtCore.QRect(570, 0, 351, 151))
        self.Sub_Title.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                     "font: 75 8pt \"Trebuchet MS\";\n"
                                     "background-color: rgb(154, 131, 175);\n"
                                     "border-color: rgb(0, 0, 0);\n"
                                     "gridline-color: rgb(0, 0, 0);")
        self.Sub_Title.setObjectName("Sub_Title")

    def setup_control_board(self):

        # sets up the frame for all the buttons and text display 
        self.Control_Board = QtWidgets.QFrame(self.centralwidget)
        self.Control_Board.setGeometry(QtCore.QRect(0, 160, 451, 691))
        self.Control_Board.setStyleSheet("background-color: rgb(70, 35, 97);")
        self.Control_Board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Control_Board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Control_Board.setObjectName("Control_Board")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Control_Board)
        self.verticalLayout.setObjectName("verticalLayout")

        # sets up another 
        self.frame_11 = QtWidgets.QFrame(self.Control_Board)
        self.frame_11.setStyleSheet("background-color: rgb(154, 131, 175);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame_5 = QtWidgets.QFrame(self.frame_11)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setStyleSheet("background-color: rgb(154, 131, 175);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")

        # sets up the arangment of buttons for instide the control board
        self.setup_control_buttons()

        # sets up the arangment of text labels for instide the control board
        self.setup_text_labels()

    def setup_control_buttons(self):

        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName("gridLayout_3")


        self.pushButton_5 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.frame_10)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 4, 0, 1, 1)


        self.pushButton_3 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.horizontalLayout.addWidget(self.frame_10)
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setStyleSheet("background-color: rgb(17, 99, 116);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")

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
        self.pushButton_10.setObjectName("pushButton_10")

    # Text labels setup
    def setup_text_labels(self):

        self.label_5 = QtWidgets.QLabel(self.frame_12)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 171, 21))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 171, 21))
        self.label_6.setObjectName("label_6")

    def setup_graphs(self):

        self.horizontalLayout.addWidget(self.frame_12)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_11)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(450, 160, 981, 691))
        self.frame_3.setStyleSheet("background-color: rgb(29, 114, 128);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # graph top left
        self.Graph_LT = QtWidgets.QWidget(self.frame_8)
        self.Graph_LT.setObjectName("Graph_LT")
        self.gridLayout_2.addWidget(self.Graph_LT, 0, 0, 1, 1)
        # graph bottom left
        self.Graph_RB = QtWidgets.QWidget(self.frame_8)
        self.Graph_RB.setObjectName("Graph_RB")
        self.gridLayout_2.addWidget(self.Graph_RB, 1, 1, 1, 1)
        # graph top right
        self.Graph_RT = QtWidgets.QWidget(self.frame_8)
        self.Graph_RT.setObjectName("Graph_RT")
        self.gridLayout_2.addWidget(self.Graph_RT, 0, 1, 1, 1)
        # graph bottom right
        self.Graph_LB = QtWidgets.QWidget(self.frame_8)
        self.Graph_LB.setObjectName("Graph_LB")
        self.gridLayout_2.addWidget(self.Graph_LB, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_8, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.display_graph_data()

    def display_graph_data(self):
        
        #set up the plots
        self.canvas1 = MplCanvas(self.Graph_LT)
        self.canvas2 = MplCanvas(self.Graph_LB)
        self.canvas3 = MplCanvas(self.Graph_RT)
        self.canvas4 = MplCanvas(self.Graph_RB)

        # Set the layout for the graphs
        self.layoutGraph1 = QtWidgets.QVBoxLayout(self.Graph_LT)
        self.layoutGraph1.addWidget(self.canvas1)

        self.layoutGraph2 = QtWidgets.QVBoxLayout(self.Graph_LB)
        self.layoutGraph2.addWidget(self.canvas2)

        self.layoutGraph3 = QtWidgets.QVBoxLayout(self.Graph_RT)
        self.layoutGraph3.addWidget(self.canvas3)

        self.layoutGraph4 = QtWidgets.QVBoxLayout(self.Graph_RB)
        self.layoutGraph4.addWidget(self.canvas4)

        # Start updating the plots
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)  # Update every second
        self.timer.timeout.connect(self.update_plots)
        self.timer.start()

    def button_functions(self):

        # designates the button to open the input box if pressed
        self.pushButton_8.clicked.connect(self.open_input_COM)

        # Connect button click to sending data to Arduino
        self.pushButton_2.clicked.connect(self.send_off)

        # Connect button click to sending data to Arduino
        self.pushButton.clicked.connect(self.send_on)

        # shows the pop up text box for setting up the COM  channel
   
    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "COM channel input"))
        # Open a dialog to ask for a COM cahnnel when the app starts
    def open_input_COM(self):

            # Open a dialog to ask for a COM cahnnel when the app starts
            text, ok = QInputDialog.getText(None, "COM Port", "Input COM channel:")

            # If the user entered the number of the channel, it will show the input in a message box and try to connect
            if ok and text:
                QMessageBox.information(None, "success :)", f"You entered: {text}")

                # Initialize serial connection
                try:
                    self.serial_port = serial.Serial(text, 9600)  # uses input to set with your Arduino port
                    time.sleep(2)  # Wait for the connection to establish

                # if there is no connection it will throw an error and catch it
                except serial.SerialException as e:
                    QMessageBox.critical(None, "Error :(", f"Failed to connect to {text}. Error: {e} (did you plug in to the pico?)")

            # if the user inputs nothing, just say uknown input
            else:
                QMessageBox.information(None, 'Error :(', "Unkown input, try again")
    
    # shows the pop up text box for setting up the COM  channel
    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", None))

    # push button that sends an on symbol
    def send_on(self):
            
        try:
            message = "on"
            self.serial_port.write(message.encode())  # Send the encoded string to the Arduino
            print("Sent: on")

        # if there is no connection it will throw an error and catch it
        except serial.SerialException as e:
            QMessageBox.critical(None, "Error :(", f"Failed to send the message. Error: {str(e)} (Did you plug into the Pico?)")
    
    # push button that sends and off symbol
    def send_off(self):
        try:
            message = "off"
            self.serial_port.write(message.encode())  # Send the encoded string to the Arduino
            print("Sent: off")
        
    # Catching any SerialException that might occur during communication
        except serial.SerialException as e:
            # Displaying the error message in a critical message box
            QMessageBox.critical(None, "Error :(", f"Failed to send the message. Error: {str(e)} (Did you plug into the Pico?)")

    # Update the graphs with data from the CSV file
    def update_plots(self):

        # Read the CSV file
        try:
            data = pd.read_csv('data - Sheet1.csv')

            # graphs 1
            self.canvas1.axes.cla()
            self.canvas1.axes.plot(data['time'], label="Time")
            self.canvas1.axes.set_ylabel("Altituide(Meters)")
            self.canvas1.axes.set_xlabel("Time(Seconds)")
            self.canvas1.axes.set_title("Altituide")
            self.canvas1.fig.tight_layout()
            self.canvas1.draw()
            # graphs 2
            self.canvas2.axes.cla()
            self.canvas2.axes.plot(data['time'], label="Time")
            self.canvas2.axes.set_ylabel("Airspeed(M/s)")
            self.canvas2.axes.set_xlabel("Time(Seconds)")
            self.canvas2.axes.set_title("Airspeed")
            self.canvas2.fig.tight_layout()
            self.canvas2.draw()
            # graphs 3
            self.canvas3.axes.cla()
            self.canvas3.axes.plot(data['time'], label="Time")
            self.canvas3.axes.set_ylabel("Altituide(Meters)")
            self.canvas3.axes.set_xlabel("Time(Seconds)")
            self.canvas3.axes.set_title("Altituide")
            self.canvas3.fig.tight_layout()
            self.canvas3.draw()
            # graphs 4
            self.canvas4.axes.cla()
            self.canvas4.axes.plot(data['time'], label="Time")
            self.canvas4.axes.set_ylabel("Altituide(Meters)")
            self.canvas4.axes.set_xlabel("Time(Seconds)")
            self.canvas4.axes.set_title("Altituide")
            self.canvas4.fig.tight_layout()
            self.canvas4.draw()

        except Exception as e:
            print(f"Error reading CSV: {e}")

    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frame.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>poop</p></body></html>"))
        self.TITLE.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>poop</p><p><br/></p></body></html>"))
        self.TITLE.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:400; color:#ffffff;\">SEA TEAM 1</span></p></body></html>"))
        self.Sub_Title.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>poop</p><p><br/></p></body></html>"))
        self.Sub_Title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:400; color:#ffffff;\">SPAROW</span></p></body></html>"))
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




# Custom class for the graph widget
class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)




import GUI_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
