# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1122, 887)
        LoginWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icone.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topbar = QtWidgets.QFrame(self.centralwidget)
        self.topbar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.topbar.setStyleSheet("")
        self.topbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topbar.setObjectName("topbar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.topbar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.topbar)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 35))
        self.frame_error.setStyleSheet("background-color: rgb(255, 44, 109);\n"
"border-radius: 10px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_error = QtWidgets.QLabel(self.frame_error)
        self.lb_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_error.setObjectName("lb_error")
        self.horizontalLayout_3.addWidget(self.lb_error)
        self.btn_error = QtWidgets.QPushButton(self.frame_error)
        self.btn_error.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_error.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    background-position: center;\n"
"    background-image: url(:/close_image/cil-x.png);\n"
"    \n"
"    background-color: rgb(10,10,10);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(55,55,55);\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(100,100,100);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.btn_error.setText("")
        self.btn_error.setObjectName("btn_error")
        self.horizontalLayout_3.addWidget(self.btn_error)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.topbar)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet("")
        self.body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout.setContentsMargins(0, 30, 0, 30)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.content = QtWidgets.QFrame(self.body)
        self.content.setMaximumSize(QtCore.QSize(450, 550))
        self.content.setStyleSheet("QFrame{\n"
"    background-color: rgb(30,30,30);\n"
"    border-radius: 10px;\n"
"}")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.logo = QtWidgets.QFrame(self.content)
        self.logo.setGeometry(QtCore.QRect(45, 45, 360, 90))
        self.logo.setMinimumSize(QtCore.QSize(360, 90))
        self.logo.setMaximumSize(QtCore.QSize(360, 90))
        self.logo.setStyleSheet("background-image: url(:/logo/logo.png);\n"
"backroung-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 6px;")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.input_user = QtWidgets.QLineEdit(self.content)
        self.input_user.setGeometry(QtCore.QRect(85, 245, 280, 50))
        self.input_user.setMinimumSize(QtCore.QSize(280, 50))
        self.input_user.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_user.setFont(font)
        self.input_user.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(105,105,105);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(65,65,65);\n"
"    color: rgb(120,120,120)\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(85,85,85);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 255, 252);\n"
"    color: rgb(200,200,200);\n"
"}")
        self.input_user.setMaxLength(32)
        self.input_user.setObjectName("input_user")
        self.input_password = QtWidgets.QLineEdit(self.content)
        self.input_password.setGeometry(QtCore.QRect(85, 305, 280, 50))
        self.input_password.setMinimumSize(QtCore.QSize(280, 50))
        self.input_password.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(105,105,105);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(65,65,65);\n"
"    color: rgb(120,120,120)\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(85,85,85);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(0, 255, 252);\n"
"    color: rgb(200,200,200);\n"
"}")
        self.input_password.setMaxLength(16)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.btn_criar_conta = QtWidgets.QPushButton(self.content)
        self.btn_criar_conta.setGeometry(QtCore.QRect(155, 480, 130, 50))
        self.btn_criar_conta.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_criar_conta.setFont(font)
        self.btn_criar_conta.setStyleSheet("QPushButton{\n"
"    background-color: rgb(30,30,30);\n"
"    border: 1px solid rgb(30,30,30);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(220,220,220);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(27, 107, 106);\n"
"}")
        self.btn_criar_conta.setObjectName("btn_criar_conta")
        self.btn_fazer_login = QtWidgets.QPushButton(self.content)
        self.btn_fazer_login.setGeometry(QtCore.QRect(85, 400, 280, 50))
        self.btn_fazer_login.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_fazer_login.setFont(font)
        self.btn_fazer_login.setStyleSheet("QPushButton{\n"
"    background-color:  rgb(80,80,80);\n"
"    border: 2px solid rgb(70,70,70);\n"
"    border-radius: 5px;\n"
"    color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(100,100,100);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(27, 107, 106);\n"
"    border: 2px solid rgb(0, 255, 252);\n"
"}")
        self.btn_fazer_login.setObjectName("btn_fazer_login")
        self.lb_novo_por_aqui = QtWidgets.QLabel(self.content)
        self.lb_novo_por_aqui.setGeometry(QtCore.QRect(158, 470, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.lb_novo_por_aqui.setFont(font)
        self.lb_novo_por_aqui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_novo_por_aqui.setStyleSheet("color :rgb(120,120,120)")
        self.lb_novo_por_aqui.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_novo_por_aqui.setObjectName("lb_novo_por_aqui")
        self.btn_forget_password = QtWidgets.QPushButton(self.content)
        self.btn_forget_password.setGeometry(QtCore.QRect(260, 365, 100, 23))
        self.btn_forget_password.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 170, 255);\n"
"    background-color: rgb(30,30,30,);\n"
"    border: 1px solid  rgb(30,30,30);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(0, 149, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(0, 149, 152);\n"
"}")
        self.btn_forget_password.setObjectName("btn_forget_password")
        self.lb_faca_login = QtWidgets.QLabel(self.content)
        self.lb_faca_login.setGeometry(QtCore.QRect(135, 155, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lb_faca_login.setFont(font)
        self.lb_faca_login.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_faca_login.setObjectName("lb_faca_login")
        self.horizontalLayout.addWidget(self.content)
        self.verticalLayout.addWidget(self.body)
        self.footer = QtWidgets.QFrame(self.centralwidget)
        self.footer.setMaximumSize(QtCore.QSize(16777215, 35))
        self.footer.setStyleSheet("background-color: rgb(15,15,15);")
        self.footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.footer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_credits = QtWidgets.QLabel(self.footer)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.lb_credits.setFont(font)
        self.lb_credits.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lb_credits.setStyleSheet("color :rgb(120,120,120)")
        self.lb_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lb_credits.setObjectName("lb_credits")
        self.verticalLayout_2.addWidget(self.lb_credits)
        self.verticalLayout.addWidget(self.footer)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Dev Claudio"))
        self.lb_error.setText(_translate("LoginWindow", "ERROR"))
        self.input_user.setPlaceholderText(_translate("LoginWindow", "USER"))
        self.input_password.setPlaceholderText(_translate("LoginWindow", "PASSWORD"))
        self.btn_criar_conta.setText(_translate("LoginWindow", "CRIAR CONTA"))
        self.btn_fazer_login.setText(_translate("LoginWindow", "FAZER LOGIN"))
        self.lb_novo_por_aqui.setText(_translate("LoginWindow", "Novo por aqui?"))
        self.btn_forget_password.setText(_translate("LoginWindow", "Esqueceu a senha?"))
        self.lb_faca_login.setText(_translate("LoginWindow", "Faça Login"))
        self.lb_credits.setText(_translate("LoginWindow", "BETA 0.1 © Created By: Claudio Lima F. "))
import file_rc_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
