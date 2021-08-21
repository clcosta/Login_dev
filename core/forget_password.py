# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgetpass.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgetPassword(object):
    def setupUi(self, ForgetPassword):
        ForgetPassword.setObjectName("ForgetPassword")
        ForgetPassword.resize(650, 400)
        ForgetPassword.setMinimumSize(QtCore.QSize(650, 400))
        ForgetPassword.setMaximumSize(QtCore.QSize(650, 400))
        self.centralwidget = QtWidgets.QWidget(ForgetPassword)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet("")
        self.body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.conteudo = QtWidgets.QFrame(self.body)
        self.conteudo.setMaximumSize(QtCore.QSize(650, 400))
        self.conteudo.setStyleSheet("QFrame{\n"
"    background-color: rgb(30,30,30);\n"
"    border-radius: 10px;\n"
"}")
        self.conteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteudo.setObjectName("conteudo")
        self.logo_2 = QtWidgets.QFrame(self.conteudo)
        self.logo_2.setGeometry(QtCore.QRect(145, 40, 360, 90))
        self.logo_2.setMinimumSize(QtCore.QSize(360, 90))
        self.logo_2.setMaximumSize(QtCore.QSize(360, 90))
        self.logo_2.setStyleSheet("background-image: url(:/logo/logo.png);\n"
"backroung-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 6px;")
        self.logo_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_2.setObjectName("logo_2")
        self.input_email = QtWidgets.QLineEdit(self.conteudo)
        self.input_email.setGeometry(QtCore.QRect(130, 230, 380, 50))
        self.input_email.setMinimumSize(QtCore.QSize(380, 50))
        self.input_email.setMaximumSize(QtCore.QSize(380, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("QLineEdit{\n"
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
        self.input_email.setMaxLength(32)
        self.input_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_email.setObjectName("input_email")
        self.btn_enviar = QtWidgets.QPushButton(self.conteudo)
        self.btn_enviar.setGeometry(QtCore.QRect(300, 300, 211, 45))
        self.btn_enviar.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_enviar.setFont(font)
        self.btn_enviar.setStyleSheet("QPushButton{\n"
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
        self.btn_enviar.setObjectName("btn_enviar")
        self.lb_description = QtWidgets.QLabel(self.conteudo)
        self.lb_description.setGeometry(QtCore.QRect(200, 190, 250, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.lb_description.setFont(font)
        self.lb_description.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_description.setStyleSheet("color :rgb(120,120,120)")
        self.lb_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_description.setObjectName("lb_description")
        self.lb_digite_seu_email = QtWidgets.QLabel(self.conteudo)
        self.lb_digite_seu_email.setGeometry(QtCore.QRect(184, 140, 285, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lb_digite_seu_email.setFont(font)
        self.lb_digite_seu_email.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_digite_seu_email.setObjectName("lb_digite_seu_email")
        self.btn_cancelar = QtWidgets.QPushButton(self.conteudo)
        self.btn_cancelar.setGeometry(QtCore.QRect(130, 300, 161, 45))
        self.btn_cancelar.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setStyleSheet("QPushButton{\n"
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
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_4.addWidget(self.conteudo)
        self.verticalLayout.addWidget(self.body)
        ForgetPassword.setCentralWidget(self.centralwidget)

        self.retranslateUi(ForgetPassword)
        QtCore.QMetaObject.connectSlotsByName(ForgetPassword)

    def retranslateUi(self, ForgetPassword):
        _translate = QtCore.QCoreApplication.translate
        ForgetPassword.setWindowTitle(_translate("ForgetPassword", "Recuperar Conta"))
        self.input_email.setPlaceholderText(_translate("ForgetPassword", "E-MAIL"))
        self.btn_enviar.setText(_translate("ForgetPassword", "ENVIAR E-MAIL"))
        self.lb_description.setText(_translate("ForgetPassword", "Um e-mail de recuperação será enviado!"))
        self.lb_digite_seu_email.setText(_translate("ForgetPassword", "Digite seu E-mail"))
        self.btn_cancelar.setText(_translate("ForgetPassword", "CANCELAR"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgetPassword = QtWidgets.QMainWindow()
    ui = Ui_ForgetPassword()
    ui.setupUi(ForgetPassword)
    ForgetPassword.show()
    sys.exit(app.exec_())