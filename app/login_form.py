# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

###################################################################
###             Author & Copyrights: TANG TRONG PHI             ###
###################################################################

from PyQt6 import QtCore, QtGui, QtWidgets
from cProfile import label
import re
from database import add_user, can_login, exist_user
import bcrypt
import json
import base64
from pathlib import Path

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1550, 850)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 400, 850))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.page_3)
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 400, 850))
        self.widget_2.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.widget_2.setObjectName("widget_2")
        self.label_login_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_login_2.setGeometry(QtCore.QRect(0, 0, 400, 850))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_login_2.setFont(font)
        self.label_login_2.setStyleSheet("border-image: url(G:/GUI/images/1357625_cp2.png);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.label_login_2.setText("")
        self.label_login_2.setObjectName("label_login_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 280, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(30, 33, 32,230);\n"
"border-radius:15px;\n"
"color:rgba(255,255,255,100);\n"
"padding-left: 20px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 350, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(30, 33, 32,230);\n"
"border-radius:15px;\n"
"color:rgba(255,255,255,100);\n"
"padding-left: 20px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 420, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(30, 33, 32,230);\n"
"border-radius:15px;\n"
"color:rgba(255,255,255,100);\n"
"padding-left: 20px;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(115, 140, 170, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setStyleSheet("color:white;\n"
"font-weight:bold;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 580, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgba(59, 61, 60,80);\n"
"border-image: url(C:/Users/_t2p/Downloads/55ovjpq6bo1dpbpq69e2m1lvrq.png);\n"
"border-radius:15px;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(parent=self.widget_2)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(135, 690, 130, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setStyleSheet("""
        QCommandLinkButton {
        color:white;
        border: none;
        font-weight: bold;
        background-color: transparent;
        font-family: Segoe UI;
        font-size: 10pt;
        }
        QCommandLinkButton:hover {
        color:red;
        background-color: rgba(113, 115, 112, 150);
        }
        """)
        icon = QtGui.QIcon.fromTheme("None")
        self.commandLinkButton_2.setIcon(icon)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(320, 800, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setGeometry(QtCore.QRect(50, 490, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;\n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(115, 50, 100, 70))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white;\n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"font-family: \"Brush Script MT\";\n"
"font-size: 28pt;")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(185, 50, 100, 70))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:red;\n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"font-family: \"Brush Script MT\";\n"
"font-size: 28pt;")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.widget = QtWidgets.QWidget(parent=self.page_4)
        self.widget.setGeometry(QtCore.QRect(0, 0, 400, 850))
        self.widget.setObjectName("widget")
        self.label_login = QtWidgets.QLabel(parent=self.widget)
        self.label_login.setEnabled(True)
        self.label_login.setGeometry(QtCore.QRect(0, 0, 400, 850))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("border-image: url(G:/GUI/images/1357625_cp2.png);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.label_login.setText("")
        self.label_login.setObjectName("label_login")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(115, 140, 170, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet("color:white;\n"
"font-weight:bold;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 300, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(30, 33, 32,230);\n"
"border-radius:15px;\n"
"color:rgba(255,255,255,100);\n"
"padding-left: 20px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 380, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(30, 33, 32,230);\n"
"border-radius:15px;\n"
"color:rgba(255,255,255,100);\n"
"padding-left: 20px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(parent=self.widget)
        self.checkBox.setGeometry(QtCore.QRect(50, 480, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("""
    QCheckBox {
        color: white;
        font-weight: bold;
        font-size: 12pt;
    }
    QCheckBox:hover {
        color: red; /* Đổi màu chữ sang đỏ khi hover */
    }
""")

        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(160, 580, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgba(59, 61, 60,80);\n"
"border-image: url(C:/Users/_t2p/Downloads/55ovjpq6bo1dpbpq69e2m1lvrq.png);\n"
"border-radius:15px;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=self.widget)
        self.commandLinkButton.setGeometry(QtCore.QRect(129, 690, 161, 40))
        self.commandLinkButton.setBaseSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setStyleSheet("""
        QCommandLinkButton {
        color:white;
        border: none;
        font-weight: bold;
        background-color: transparent;
        font-family: Segoe UI;
        font-size: 10pt;
        }
        QCommandLinkButton:hover {
        color:red;
        background-color: rgba(113, 115, 112, 150);
        }
        """)
        icon = QtGui.QIcon.fromTheme("None")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(320, 800, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(115, 50, 100, 70))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;\n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"font-family: \"Brush Script MT\";\n"
"font-size: 28pt;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(185, 50, 100, 70))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:red;\n"
"border: none;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"font-family: \"Brush Script MT\";\n"
"font-size: 28pt;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(parent=self.widget)
        self.label_14.setGeometry(QtCore.QRect(50, 510, 300, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:red;\n"
                                    "border: none;\n"
                                    "font-weight: bold;\n"
                                    "background-color: transparent;")
        self.label_14.setText("")
        self.label_14.setAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_14.setObjectName("label_14")
        self.label_login.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.checkBox.raise_()
        self.commandLinkButton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_14.raise_()
        self.stackedWidget.addWidget(self.page_4)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=Form)
        self.stackedWidget_2.setGeometry(QtCore.QRect(400, 0, 1150, 850))
        self.stackedWidget_2.setStyleSheet("border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(G:/GUI/images/ss_cp.jpg);\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_11 = QtWidgets.QLabel(parent=self.page_2)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-image: url(G:/GUI/images/female-psychologist-consulting-patient-desk-hospital.jpg);\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_12 = QtWidgets.QLabel(parent=self.page_5)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-image: url(G:/GUI/images/assortment-fresh-vegetables-herbs.jpg);\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_16 = QtWidgets.QLabel(parent=self.page_6)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("border-image: url(G:/GUI/images/woman-stretching-her-legs-with-statistics-background.jpg);\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_13 = QtWidgets.QLabel(parent=self.page_7)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border-image: url(G:/GUI/images/winter_cr.png);\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.stackedWidget_2.addWidget(self.page_7)
        self.close_button = QtWidgets.QPushButton(parent=Form)
        self.close_button.setGeometry(QtCore.QRect(1520, 0, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet("""
        QPushButton {
        border-top-right-radius:10px;
        color: white;
        boder:none;
        font-family: "Bauhaus 93";
        font-size: 14pt;
        }
        QPushButton:hover {
        background-color: rgba(245, 69, 66, 180);
        }
""")
        self.close_button.setObjectName("close_button")
        self.minimize_button = QtWidgets.QPushButton(parent=Form)
        self.minimize_button.setGeometry(QtCore.QRect(1490, 0, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.minimize_button.setFont(font)
        self.minimize_button.setMouseTracking(False)
        self.minimize_button.setStyleSheet("""
        QPushButton {
        border:none;
        color:white;
        font-weight:bold;
        font-family: "Bauhaus 93";
        font-size: 14pt;
        }
        QPushButton:hover {
        background-color: rgba(113, 115, 112, 180);
        }
        """)
        self.minimize_button.setObjectName("minimize_button")
        self.stackedWidget_2.raise_()
        self.stackedWidget.raise_()
        self.close_button.raise_()
        self.minimize_button.raise_()

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #################################################################
        ## XỬ LÝ GIAO DIỆN NÂNG CAO Ở ĐÂY                              ##
        #################################################################

        ## Custom minimize & close
        self.minimize_button.clicked.connect(Form.showMinimized)
        self.close_button.clicked.connect(Form.close)

        ## Cắt Form cho đẹp giao diện
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint) #Bỏ viền cửa sổ
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground) #Nền form trong suốt

        ## Tạo slide show cho stackedWidget bên phải
        # Tạo QTimer
        self.timer = QtCore.QTimer(Form)
        self.timer.timeout.connect(self.switch_page)
        self.timer.start(5000)  # Đặt thời gian là 3000 ms (3 giây)

        ## Highlights nút đăng nhập và đăng ký
        # Khi không rỗng các trường tài khoản mật khẩu thì HL
        self.lineEdit.textChanged.connect(self.check_inputs_login)
        self.lineEdit_2.textChanged.connect(self.check_inputs_login)

        self.lineEdit_3.textChanged.connect(self.check_inputs_signup)
        self.lineEdit_4.textChanged.connect(self.check_inputs_signup)
        self.lineEdit_5.textChanged.connect(self.check_inputs_signup)

        ## Che mật khẩu
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        #################################################################
        ## XỬ LÝ SỰ KIỆN CHO CÁC NÚT Ở ĐÂY                             ##
        #################################################################

        ## Chuyển trang đăng nhập - đăng ký
        self.commandLinkButton.clicked.connect(lambda: self.sign_up_or_login(0))
        self.commandLinkButton_2.clicked.connect(lambda: self.sign_up_or_login(1))

        ## Disable mặc định cho một số nút
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.signup)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "TÊN NGƯỜI DÙNG"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "MẬT KHẨU"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "XÁC NHẬN MẬT KHẨU"))
        self.label_5.setText(_translate("Form", "Đăng ký"))
        self.commandLinkButton_2.setText(_translate("Form", "Đã có tài khoản?"))
        self.label_6.setText(_translate("Form", "v1.0.0"))
        self.label_10.setText(_translate("Form", "Care"))
        self.label_9.setText(_translate("Form", "Center"))
        self.label_4.setText(_translate("Form", "Đăng nhập"))
        self.lineEdit.setPlaceholderText(_translate("Form", "TÊN NGƯỜI DÙNG"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "MẬT KHẨU"))
        self.checkBox.setText(_translate("Form", "GHI NHỚ ĐĂNG NHẬP"))
        self.commandLinkButton.setText(_translate("Form", "Chưa có tài khoản?"))
        self.label_3.setText(_translate("Form", "v1.0.0"))
        self.label_7.setText(_translate("Form", "Care"))
        self.label_8.setText(_translate("Form", "Center"))
        self.close_button.setText(_translate("Form", "x"))
        self.minimize_button.setText(_translate("Form", "_"))

    ####################################################################
    ##          CÁC HÀM XỬ LÝ GIAO DIỆN NÂNG CAO Ở ĐÂY                ##
    ####################################################################
    def switch_page(self):
            # Lấy trang hiện tại
            current_index = self.stackedWidget_2.currentIndex()

            # Chuyển sang trang kế tiếp (vòng tròn)
            next_index = (current_index + 1) % self.stackedWidget_2.count()
            self.stackedWidget_2.setCurrentIndex(next_index)

    #################
    ## Các trường điền filled thì enable nút bấm và highlights
    def update_button_style(self, button, enabled):
            """
            Cập nhật kiểu giao diện cho nút bấm dựa trên trạng thái enabled.
            """
            if enabled:
                    button.setStyleSheet("""
            QPushButton {
                background-color: rgba(59, 61, 60, 200);
                border-image: url(C:/Users/_t2p/Downloads/55ovjpq6bo1dpbpq69e2m1lvrq.png);
                border-radius: 15px;
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(240, 44, 5, 200);
            }""")
                    button.setDisabled(False)
            else:
                    button.setStyleSheet("""
            QPushButton {
                background-color: rgba(59, 61, 60, 80);
                border-image: url(C:/Users/_t2p/Downloads/55ovjpq6bo1dpbpq69e2m1lvrq.png);
                border-radius: 15px;
                border: none;
            }""")
                    button.setDisabled(True)

    def check_inputs(self, line_edits, button):
            """
            Kiểm tra nếu tất cả các trường input có giá trị, sau đó cập nhật nút bấm.

            Args:
                line_edits (list): Danh sách các trường QLineEdit cần kiểm tra.
                button (QPushButton): Nút bấm cần cập nhật.
            """
            all_filled = all(line_edit.text().strip() for line_edit in line_edits)
            self.update_button_style(button, all_filled)

    def check_inputs_login(self):
            self.check_inputs([self.lineEdit, self.lineEdit_2], self.pushButton)

    def check_inputs_signup(self):
            self.check_inputs([self.lineEdit_3, self.lineEdit_4, self.lineEdit_5], self.pushButton_2)

    def update_label(self, label, text, color):
            label.setStyleSheet(f"color: {color}; border: none; font-weight: bold; background-color: transparent;")
            label.setText(text)

    def clear_signup_form(self):
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()

    ####################################################################
    ##          CÁC HÀM XỬ LÝ BACKEND CHO LOGIN/SIGN UP Ở ĐÂY         ##
    ####################################################################

    def sign_up_or_login(self, code):
            if code == 0:
                self.stackedWidget.setCurrentIndex(0)
                self.label.setText("")
                self.clear_signup_form()
            else:
                self.stackedWidget.setCurrentIndex(1)

    def login(self):
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()

            if not self.is_valid_username(username):
                    self.update_label(self.label_14, "Đăng nhập thất bại!", "red")
                    return

            if not self.is_valid_password(password):
                    self.update_label(self.label_14, "Đăng nhập thất bại!", "red")
                    return

            if can_login(username, password):
                    self.update_label(self.label_14, "Đăng nhập thành công!", "green")
                    self.save_login_info(username, password if self.checkBox.isChecked() else None,
                                         self.checkBox.isChecked())
            else:
                    self.update_label(self.label_14, "Đăng nhập thất bại!", "red")

    def signup(self):
            username = self.lineEdit_3.text()
            password = self.lineEdit_4.text()
            confirm_password = self.lineEdit_5.text()

            error_messages = []
            if not self.is_valid_username(username):
                    error_messages.append("Tên đăng nhập không hợp lệ.")
            if not self.is_valid_password(password):
                    error_messages.append("Mật khẩu phải có ít nhất 8 kí tự.")
            elif password != confirm_password:
                    error_messages.append("Xác nhận mật khẩu không khớp.")

            if exist_user(username):
                    error_messages.append("Tên đăng nhập đã tồn tại.")

            if error_messages:
                    self.update_label(self.label, "\n".join(error_messages), "red")
                    return

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            add_user(username, hashed_password)
            self.update_label(self.label, "Đăng ký thành công!", "green")
            self.clear_signup_form()


    def is_valid_username(self, username):
            # Biểu thức chính quy để kiểm tra điều kiện
            pattern = r'^[A-Za-z][A-Za-z0-9_]{2,29}$'
            if re.match(pattern, username):
                    return True
            return False

    def is_valid_password(self, password):
            # Biểu thức chính quy để kiểm tra điều kiện
            pattern = r'^.{8,}$'
            if re.match(pattern, password):
                    return True
            return False

    def check_password(self, password, hashed_password):
            password_bytes = password.encode('utf-8')
            return bcrypt.checkpw(password_bytes, hashed_password.encode('utf-8'))

    def save_login_info(self, username, password, remember_me):
            config_dir = Path(__file__).resolve().parent.parent / 'config'
            config_dir.mkdir(parents=True, exist_ok=True)
            login_file = config_dir / 'login.json'

            encrypted_username = base64.b64encode(username.encode('utf-8')).decode('utf-8') if username is not None else None
            encrypted_password = base64.b64encode(password.encode('utf-8')).decode('utf-8') if password is not None else None
            data = {'username': encrypted_username, 'password': encrypted_password, 'remember_me': remember_me}
            with open(login_file, 'w') as file:
                    json.dump(data, file)

    def load_login_info(self):
            config_dir = Path(__file__).resolve().parent.parent / 'config'
            login_file = config_dir / 'login.json'
            try:
                    with open(login_file, 'r') as file:
                            data = json.load(file)
                            username = base64.b64decode(data['username'].encode('utf-8')).decode('utf-8') if data['username'] is not None else None
                            password = base64.b64decode(data['password'].encode('utf-8')).decode('utf-8') if data['password'] is not None else None
                            remember_me = data['remember_me']
                            return username, password, remember_me
            except (FileNotFoundError, KeyError):
                    return None, None, False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    username, password, remember_me = ui.load_login_info()
    ui.lineEdit.setText(username)
    ui.lineEdit_2.setText(password)
    ui.checkBox.setChecked(remember_me)
    sys.exit(app.exec())
