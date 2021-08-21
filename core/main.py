import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from .cores import (INPUT_ERROR, INPUT_OK, LABEL_ERROR, LABEL_VERDE,
                    POPUP_ERROR, POPUP_OK)
from .create_account import Ui_CreatedAccountWindow
from .forget_password import Ui_ForgetPassword
from .login import Ui_LoginWindow


class CreateAccount(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.account = Ui_CreatedAccountWindow()
        self.account.setupUi(self)

        self.account.btn_fazer_login.clicked.connect(self.abrir_janela_fazer_login)

        ### Botão fechar PopPup Error
        self.account.btn_close_popup.clicked.connect(self.close_popup)

        ### Esconder PopPup error 
        self.account.frame_error.hide()

        ### Criar a conta e verificar os campos
        self.account.btn_criar_conta.clicked.connect(self.checkFilds)

        self.show()

    def close_popup(self):
        self.account.frame_error.hide()
        if self.account.input_nome:
            self.account.input_nome.setStyleSheet(INPUT_OK)
        if self.account.input_user:
            self.account.input_user.setStyleSheet(INPUT_OK)
        if self.account.input_email:
            self.account.input_email.setStyleSheet(INPUT_OK)
        if self.account.input_password1:
            self.account.input_password1.setStyleSheet(INPUT_OK)
        if self.account.input_password2:
            self.account.input_password2.setStyleSheet(INPUT_OK)

    def checkFilds(self):
        text_nome = ''
        text_user = ''
        text_email = ''
        text_password1 = ''
        text_password2 = ''
        erros = 0

        # Show Message in PoPup error
        def showMessage(message):
            self.account.frame_error.show()
            self.account.lb_popup_error.setText(message)

        # Check Nome
        if not self.account.input_nome.text():
            text_nome = " Nome inválido "
            self.account.input_nome.setStyleSheet(INPUT_ERROR)
            erros += 1
        else:
            text_nome = ""
        
        # Check User
        if not self.account.input_user.text():
            text_user = " Usuário inválido "
            self.account.input_user.setStyleSheet(INPUT_ERROR)
            erros += 1    
        else:
            text_user = ""

        # Check E-mail
        if not self.account.input_email.text():
            text_email = " E-mail inválido "
            self.account.input_email.setStyleSheet(INPUT_ERROR)
            erros += 1
        else:
            if '@' not in self.account.input_email.text() or '.' not in self.account.input_email.text():
                text_email = " E-mail inválido "
                self.account.input_email.setStyleSheet(INPUT_ERROR)
                erros += 1
            else:
                text_email = ""
        
        # Check Password1
        if not self.account.input_password1.text():
            text_password1 = " Senha inválida "
            self.account.input_password1.setStyleSheet(INPUT_ERROR)
            erros += 1
        else:
            text_password1 = ""
        
        # Check Password2
        if not self.account.input_password1.text():
            text_password2 = " Senha inválida "
            self.account.input_password1.setStyleSheet(INPUT_ERROR)
            erros += 1
        else:
            if self.account.input_password2.text() != self.account.input_password1.text():
                text_password2 = " As senhas devem ser iguais "
                self.account.input_password1.setStyleSheet(INPUT_ERROR)
                self.account.input_password2.setStyleSheet(INPUT_ERROR)
                erros += 1
            else:
                text_password2 = ""

        # Check both Fields
        if text_user + text_password1 + text_nome + text_email + text_password2 != '':
            if erros >= 3:
                account_status = " Preencha todos os campos corretamente "
            else:
                account_status = text_user + text_password1 + text_nome + text_email + text_password2
            showMessage(account_status)
            self.account.frame_error.setStyleSheet(POPUP_ERROR)
        else:
            account_status = " Conta criada com sucesso "
            self.account.input_password1.setStyleSheet(INPUT_OK)
            self.account.input_password2.setStyleSheet(INPUT_OK)
            self.account.input_email.setStyleSheet(INPUT_OK)
            self.account.input_nome.setStyleSheet(INPUT_OK)
            self.account.input_user.setStyleSheet(INPUT_OK)
            self.account.frame_error.setStyleSheet(POPUP_OK)
            showMessage(account_status)


    def abrir_janela_fazer_login(self):
        login_window = LoginWindow()
        self.hide()
        self.ui = login_window


class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.btn_criar_conta.clicked.connect(self.abrir_janela_criar_conta)
        
        ### Botão fechar PopPup Error
        self.ui.btn_error.clicked.connect(self.close_popup)

        ### Esconder PopPup error 
        self.ui.frame_error.hide()

        ### Fazer Login e verificar os campos
        self.ui.btn_fazer_login.clicked.connect(self.checkFilds)

        ### Botao de Esqueceu a senha
        self.ui.btn_forget_password.clicked.connect(self.abrir_janela_esqueci_senha)

        self.show()

    def close_popup(self):
        self.ui.frame_error.hide()
        if self.ui.input_user:
            self.ui.input_user.setStyleSheet(INPUT_OK)
        if self.ui.input_password:
            self.ui.input_password.setStyleSheet(INPUT_OK)

    def checkFilds(self):
        text_user = ''
        text_password = ''

        # Show Message in PoPup error
        def showMessage(message):
            self.ui.frame_error.show()
            self.ui.lb_error.setText(message)

        # Check User
        if not self.ui.input_user.text():
            text_user = " Usuário inválido "
            self.ui.input_user.setStyleSheet(INPUT_ERROR)
        else:
            text_user = ""

        # Check Password
        if not self.ui.input_password.text():
            text_password = " Senha inválida "
            self.ui.input_password.setStyleSheet(INPUT_ERROR)
        else:
            text_password = ""
        
        # Check both Fields
        if text_user + text_password != '':
            login_status = text_user + text_password
            showMessage(login_status)
            self.ui.frame_error.setStyleSheet(POPUP_ERROR)
        else:
            login_status = " Login efetuado com sucesso "
            self.ui.input_password.setStyleSheet(INPUT_OK)
            self.ui.input_user.setStyleSheet(INPUT_OK)
            self.ui.frame_error.setStyleSheet(POPUP_OK)
            showMessage(login_status)

    def abrir_janela_criar_conta(self):
        account_window = CreateAccount()
        self.hide()
        self.ui = account_window

    def abrir_janela_esqueci_senha(self):
        forget_window = ForgetPassword()
        self.hide()
        self.ui = forget_window


class ForgetPassword(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ForgetPassword()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ### BTN CLOSE WINDOW
        self.ui.btn_cancelar.clicked.connect(self.fechar_forget)

        ### BTN SEND EMAIL
        self.ui.btn_enviar.clicked.connect(self.checkFilds)


        self.show()

    def checkFilds(self):
            text_email = ''

            # Show Message in PoPup error
            def showMessage(message):
                self.ui.lb_digite_seu_email.setText(message)

            # Check E-mail
            if not self.ui.input_email.text():
                text_email = " E-mail inválido "
                self.ui.input_email.setStyleSheet(INPUT_ERROR)
            else:
                if '@' not in self.ui.input_email.text() or '.' not in self.ui.input_email.text():
                    text_email = " E-mail inválido "
                    self.ui.input_email.setStyleSheet(INPUT_ERROR)
                else:
                    text_email = ""

            if text_email != '':
                email_status = text_email
                showMessage(email_status)
                self.ui.lb_digite_seu_email.setStyleSheet(LABEL_ERROR)
            else:
                email_status = " Email enviado !"
                self.ui.lb_digite_seu_email.setStyleSheet(LABEL_VERDE)
                self.ui.input_email.setStyleSheet(INPUT_OK)
                showMessage(email_status)

    def fechar_forget(self):
        login_window = LoginWindow()
        self.hide()
        self.ui = login_window
