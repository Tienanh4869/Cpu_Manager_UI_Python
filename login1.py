# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI_Login(object):
    def setupUi(self, UI_Login):
        UI_Login.setObjectName("UI_Login")
        UI_Login.setWindowModality(QtCore.Qt.WindowModal)
        UI_Login.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        UI_Login.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        UI_Login.resize(744, 633)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        UI_Login.setFont(font)
        UI_Login.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/hinh/image/cpu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UI_Login.setWindowIcon(icon)
        UI_Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        UI_Login.setAutoFillBackground(True)
        self.widget = QtWidgets.QWidget(UI_Login)
        self.widget.setGeometry(QtCore.QRect(110, 40, 561, 581))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: transparent;")
        self.widget.setObjectName("widget")
        self.lb_bg_left = QtWidgets.QLabel(self.widget)
        self.lb_bg_left.setGeometry(QtCore.QRect(0, 0, 281, 581))
        self.lb_bg_left.setStyleSheet("border-image: url(:/hinh/image/amdpnx.png);\n"
"\n"
"border-top-left-radius: 100px;\n"
"")
        self.lb_bg_left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lb_bg_left.setText("")
        self.lb_bg_left.setScaledContents(True)
        self.lb_bg_left.setObjectName("lb_bg_left")
        self.lb_bg_right = QtWidgets.QLabel(self.widget)
        self.lb_bg_right.setGeometry(QtCore.QRect(280, 0, 281, 581))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.lb_bg_right.setFont(font)
        self.lb_bg_right.setStyleSheet("background-color: rgba(255, 255, 255);\n"
"border-bottom-right-radius:100px")
        self.lb_bg_right.setText("")
        self.lb_bg_right.setObjectName("lb_bg_right")
        self.le_us = QtWidgets.QLineEdit(self.widget)
        self.le_us.setGeometry(QtCore.QRect(321, 180, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setUnderline(True)
        font.setKerning(False)
        self.le_us.setFont(font)
        self.le_us.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0,0, 0, 240);\n"
"")
        self.le_us.setFrame(False)
        self.le_us.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_us.setDragEnabled(False)
        self.le_us.setReadOnly(False)
        self.le_us.setObjectName("le_us")
        self.le_pw = QtWidgets.QLineEdit(self.widget)
        self.le_pw.setGeometry(QtCore.QRect(321, 246, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setUnderline(True)
        font.setKerning(False)
        self.le_pw.setFont(font)
        self.le_pw.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0,0, 0, 240);\n"
"")
        self.le_pw.setFrame(False)
        self.le_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_pw.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_pw.setDragEnabled(False)
        self.le_pw.setReadOnly(False)
        self.le_pw.setObjectName("le_pw")
        self.pb_login = QtWidgets.QPushButton(self.widget)
        self.pb_login.setGeometry(QtCore.QRect(330, 350, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pb_login.setFont(font)
        self.pb_login.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 255, 255);\n"
"    color: black;\n"
"    border: 1px solid black;     /* viền đen */\n"
"\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #ffffcc,  /* vàng trắng nhạt */\n"
"        stop:1 #fff176   /* vàng nhạt */\n"
"    );\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #ffb74d,  /* cam nhạt */\n"
"        stop:1 #f57c00   /* cam đậm */\n"
"    );\n"
"    color: black;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/hinh/image/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_login.setIcon(icon1)
        self.pb_login.setObjectName("pb_login")
        self.cb_show = QtWidgets.QCheckBox(self.widget)
        self.cb_show.setGeometry(QtCore.QRect(390, 300, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.cb_show.setFont(font)
        self.cb_show.setObjectName("cb_show")
        self.lb_logo = QtWidgets.QLabel(self.widget)
        self.lb_logo.setGeometry(QtCore.QRect(310, -20, 221, 191))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_logo.setFont(font)
        self.lb_logo.setStyleSheet("")
        self.lb_logo.setText("")
        self.lb_logo.setTextFormat(QtCore.Qt.RichText)
        self.lb_logo.setPixmap(QtGui.QPixmap(":/hinh/image/logo1.png"))
        self.lb_logo.setScaledContents(True)
        self.lb_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_logo.setObjectName("lb_logo")
        self.lb_to_signup = QtWidgets.QLabel(self.widget)
        self.lb_to_signup.setGeometry(QtCore.QRect(320, 460, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lb_to_signup.setFont(font)
        self.lb_to_signup.setObjectName("lb_to_signup")
        self.lb_ico_dont_have_account = QtWidgets.QLabel(self.widget)
        self.lb_ico_dont_have_account.setGeometry(QtCore.QRect(280, 435, 51, 51))
        self.lb_ico_dont_have_account.setText("")
        self.lb_ico_dont_have_account.setPixmap(QtGui.QPixmap(":/hinh/image/problem.png"))
        self.lb_ico_dont_have_account.setScaledContents(True)
        self.lb_ico_dont_have_account.setObjectName("lb_ico_dont_have_account")
        self.lb_icon_usn = QtWidgets.QLabel(self.widget)
        self.lb_icon_usn.setGeometry(QtCore.QRect(290, 190, 31, 31))
        self.lb_icon_usn.setText("")
        self.lb_icon_usn.setPixmap(QtGui.QPixmap(":/hinh/image/user.png"))
        self.lb_icon_usn.setScaledContents(True)
        self.lb_icon_usn.setObjectName("lb_icon_usn")
        self.lb_icon_lock = QtWidgets.QLabel(self.widget)
        self.lb_icon_lock.setGeometry(QtCore.QRect(280, 250, 41, 41))
        self.lb_icon_lock.setText("")
        self.lb_icon_lock.setPixmap(QtGui.QPixmap(":/hinh/image/lock.png"))
        self.lb_icon_lock.setScaledContents(True)
        self.lb_icon_lock.setObjectName("lb_icon_lock")
        self.exit = QtWidgets.QPushButton(UI_Login)
        self.exit.setGeometry(QtCore.QRect(680, 0, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 255, 255);\n"
"    color: black;\n"
"    border: 1px solid black;     /* viền đen */\n"
"\n"
"    border-radius: 20px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #ffffcc,  /* vàng trắng nhạt */\n"
"        stop:1 #fff176   /* vàng nhạt */\n"
"    );\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #ffb74d,  /* cam nhạt */\n"
"        stop:1 #f57c00   /* cam đậm */\n"
"    );\n"
"    color: black;\n"
"}\n"
"")
        self.exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/hinh/image/reject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon2)
        self.exit.setObjectName("exit")
        self.label = QtWidgets.QLabel(UI_Login)
        self.label.setGeometry(QtCore.QRect(110, 0, 31, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/hinh/image/link.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(UI_Login)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 91, 31))
        self.label_3.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"border-radius:15px;\n"
"    border: 1px solid black;   ")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(UI_Login)
        self.label_2.setGeometry(QtCore.QRect(150, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(UI_Login)
        self.label_4.setGeometry(QtCore.QRect(110, 0, 28, 29))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/hinh/image/login.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(UI_Login)
        QtCore.QMetaObject.connectSlotsByName(UI_Login)

    def retranslateUi(self, UI_Login):
        _translate = QtCore.QCoreApplication.translate
        UI_Login.setWindowTitle(_translate("UI_Login", "Quản lí CPU TTA"))
        self.le_us.setPlaceholderText(_translate("UI_Login", "User Name"))
        self.le_pw.setPlaceholderText(_translate("UI_Login", "Password"))
        self.pb_login.setText(_translate("UI_Login", "Log In"))
        self.cb_show.setText(_translate("UI_Login", "Show password"))
        self.lb_to_signup.setText(_translate("UI_Login", "<html><head/><body><p>Don\'t have an account ? <a href=\"#\"><span style=\" text-decoration: underline; color:#0000ff;\">SIGN UP</span></a></p></body></html>"))
        self.label_2.setText(_translate("UI_Login", "Login"))
import Cpu_hinh


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UI_Login = QtWidgets.QWidget()
    ui = Ui_UI_Login()
    ui.setupUi(UI_Login)
    UI_Login.show()
    sys.exit(app.exec_())
