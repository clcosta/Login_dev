# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'created_account.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreatedAccountWindow(object):
    def setupUi(self, CreatedAccountWindow):
        CreatedAccountWindow.setObjectName("CreatedAccountWindow")
        CreatedAccountWindow.resize(1126, 886)
        CreatedAccountWindow.setMinimumSize(QtCore.QSize(500, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icone/icone.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreatedAccountWindow.setWindowIcon(icon)
        CreatedAccountWindow.setStyleSheet("background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(CreatedAccountWindow)
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_5.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lb_popup_error = QtWidgets.QLabel(self.frame_error)
        self.lb_popup_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_popup_error.setObjectName("lb_popup_error")
        self.horizontalLayout_5.addWidget(self.lb_popup_error)
        self.btn_close_popup = QtWidgets.QPushButton(self.frame_error)
        self.btn_close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_close_popup.setStyleSheet("QPushButton {\n"
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
        self.btn_close_popup.setText("")
        self.btn_close_popup.setObjectName("btn_close_popup")
        self.horizontalLayout_5.addWidget(self.btn_close_popup)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.topbar)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet("")
        self.body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.content = QtWidgets.QFrame(self.body)
        self.content.setMaximumSize(QtCore.QSize(450, 700))
        self.content.setStyleSheet("QFrame{\n"
"    background-color: rgb(30,30,30);\n"
"    border-radius: 10px;\n"
"}")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.input_nome = QtWidgets.QLineEdit(self.content)
        self.input_nome.setGeometry(QtCore.QRect(85, 220, 280, 50))
        self.input_nome.setMinimumSize(QtCore.QSize(280, 50))
        self.input_nome.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_nome.setFont(font)
        self.input_nome.setStyleSheet("QLineEdit{\n"
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
        self.input_nome.setMaxLength(32)
        self.input_nome.setObjectName("input_nome")
        self.input_user = QtWidgets.QLineEdit(self.content)
        self.input_user.setGeometry(QtCore.QRect(85, 280, 280, 50))
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
        self.input_email = QtWidgets.QLineEdit(self.content)
        self.input_email.setGeometry(QtCore.QRect(85, 340, 280, 50))
        self.input_email.setMinimumSize(QtCore.QSize(280, 50))
        self.input_email.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
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
        self.input_email.setObjectName("input_email")
        self.input_password1 = QtWidgets.QLineEdit(self.content)
        self.input_password1.setGeometry(QtCore.QRect(85, 400, 280, 50))
        self.input_password1.setMinimumSize(QtCore.QSize(280, 50))
        self.input_password1.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_password1.setFont(font)
        self.input_password1.setStyleSheet("QLineEdit{\n"
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
        self.input_password1.setMaxLength(16)
        self.input_password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password1.setObjectName("input_password1")
        self.lb_criar_conta = QtWidgets.QLabel(self.content)
        self.lb_criar_conta.setGeometry(QtCore.QRect(135, 150, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lb_criar_conta.setFont(font)
        self.lb_criar_conta.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_criar_conta.setObjectName("lb_criar_conta")
        self.lb_ja_tem_conta = QtWidgets.QLabel(self.content)
        self.lb_ja_tem_conta.setGeometry(QtCore.QRect(150, 610, 150, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.lb_ja_tem_conta.setFont(font)
        self.lb_ja_tem_conta.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_ja_tem_conta.setStyleSheet("color :rgb(120,120,120)")
        self.lb_ja_tem_conta.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_ja_tem_conta.setObjectName("lb_ja_tem_conta")
        self.btn_fazer_login = QtWidgets.QPushButton(self.content)
        self.btn_fazer_login.setGeometry(QtCore.QRect(160, 630, 130, 50))
        self.btn_fazer_login.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_fazer_login.setFont(font)
        self.btn_fazer_login.setStyleSheet("QPushButton{\n"
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
        self.btn_fazer_login.setObjectName("btn_fazer_login")
        self.input_password2 = QtWidgets.QLineEdit(self.content)
        self.input_password2.setGeometry(QtCore.QRect(85, 460, 280, 50))
        self.input_password2.setMinimumSize(QtCore.QSize(280, 50))
        self.input_password2.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_password2.setFont(font)
        self.input_password2.setStyleSheet("QLineEdit{\n"
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
        self.input_password2.setMaxLength(16)
        self.input_password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password2.setObjectName("input_password2")
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
        self.btn_criar_conta = QtWidgets.QPushButton(self.content)
        self.btn_criar_conta.setGeometry(QtCore.QRect(85, 550, 280, 50))
        self.btn_criar_conta.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_criar_conta.setFont(font)
        self.btn_criar_conta.setStyleSheet("QPushButton{\n"
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
        self.btn_criar_conta.setObjectName("btn_criar_conta")
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
        CreatedAccountWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreatedAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(CreatedAccountWindow)

    def retranslateUi(self, CreatedAccountWindow):
        _translate = QtCore.QCoreApplication.translate
        CreatedAccountWindow.setWindowTitle(_translate("CreatedAccountWindow", "Dev Claudio"))
        self.lb_popup_error.setText(_translate("CreatedAccountWindow", "ERROR"))
        self.input_nome.setPlaceholderText(_translate("CreatedAccountWindow", "NOME"))
        self.input_user.setPlaceholderText(_translate("CreatedAccountWindow", "USER"))
        self.input_email.setPlaceholderText(_translate("CreatedAccountWindow", "E-MAIL"))
        self.input_password1.setPlaceholderText(_translate("CreatedAccountWindow", "STRONG PASSWORD"))
        self.lb_criar_conta.setText(_translate("CreatedAccountWindow", "Criar conta"))
        self.lb_ja_tem_conta.setText(_translate("CreatedAccountWindow", "J?? tem uma conta?"))
        self.btn_fazer_login.setText(_translate("CreatedAccountWindow", "Fazer login"))
        self.input_password2.setPlaceholderText(_translate("CreatedAccountWindow", "REPEAT PASSWORD"))
        self.btn_criar_conta.setText(_translate("CreatedAccountWindow", "Criar Conta"))
        self.lb_credits.setText(_translate("CreatedAccountWindow", "BETA 0.1 ?? Created By: Claudio Lima F. "))
import file_rc_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreatedAccountWindow = QtWidgets.QMainWindow()
    ui = Ui_CreatedAccountWindow()
    ui.setupUi(CreatedAccountWindow)
    CreatedAccountWindow.show()
    sys.exit(app.exec_())
