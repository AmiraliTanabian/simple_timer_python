
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        self.hour = 0 
        self.second = 0 
        self.minute = 0 
        self.countClicked = 0


        Form.setObjectName("Form")
        # Form.resize(400, 274)
        Form.setMinimumSize(QtCore.QSize(400, 247))
        Form.setMaximumSize(QtCore.QSize(400, 247))
        font = QtGui.QFont()
        font.setPointSize(20)
        Form.setFont(font)
        self.lcdNumber = QtWidgets.QLCDNumber(parent=Form)
        self.lcdNumber.display("0:0:0")
        self.lcdNumber.setGeometry(QtCore.QRect(40, 40, 311, 141))
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setBaseSize(QtCore.QSize(0, 0))
        self.lcdNumber.setStyleSheet("border:none;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 88, 27))
        font = QtGui.QFont()
        font.setFamily("Noto Serif Lao Blk")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("background:green;\n"
"\n"
"")
        self.pushButton.clicked.connect(self.start_timer_btn_func)
        self.pushButton.setObjectName("pushButton")



        self.earase_btn = QtWidgets.QPushButton(parent=Form)
        self.earase_btn.setGeometry(QtCore.QRect(160, 220, 88, 27))
        self.earase_btn.setFont(font)
        self.earase_btn.setText('Erase')
        self.earase_btn.setDisabled(True)
        self.earase_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.earase_btn.setStyleSheet("background:gray;\n"
"\n"
"")
        self.earase_btn.clicked.connect(self.erase_btn_func)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Timer"))
        self.pushButton.setText(_translate("Form", "Start"))

        self.Timer = QtCore.QTimer()
        self.Timer.timeout.connect(self.set_time)

    def start_timer_btn_func(self):
        self.countClicked += 1 
        self.earase_btn.setEnabled(True)
        
        print(self.countClicked)
        # Clicked on "Start" button
        if self.countClicked % 2 != 0 : 

            self.pushButton.setText('Pause')
            self.pushButton.setStyleSheet("background-color:red;")
            self.Timer.start(1000)
        
        # Clicked on stop buttn 
        else : 
            self.pushButton.setStyleSheet("background:green;")
            self.pushButton.setText("Start")            
            self.Timer.stop()







    def set_time(self):
        
        


        self.second += 1 

        if self.second == 60 :
            self.second = 0 
            self.minute += 1 

        if self.minute == 60 : 
            self.minute = 0 
            self.hour += 1 

        self.lcdNumber.display("%s:%s:%s" %(self.hour, self.minute, self.second))

    def erase_btn_func(self):
            self.lcdNumber.display("00:00:00")
            self.hour = 0 
            self.minute = 0 
            self.second = 0 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
