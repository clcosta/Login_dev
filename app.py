if __name__ == "__main__":
    from core.main import *

    app = QApplication(sys.argv)
    login_window = LoginWindow()
    sys.exit(app.exec_())
