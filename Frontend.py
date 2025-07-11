from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout,
    QHBoxLayout, QDateTimeEdit, QMessageBox
)
from PyQt5.QtCore import Qt,QTimer
import sys
import backend


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Login")

        # Email
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Digite seu email")

        # Senha
        self.password_label = QLabel("Senha:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Digite sua senha")

        # Botão mostrar/ocultar senha
        self.toggle_password_btn = QPushButton("Mostrar")
        self.toggle_password_btn.setCheckable(True)
        self.toggle_password_btn.toggled.connect(self.toggle_password_visibility)

        # Layout para senha + botão
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.toggle_password_btn)

        # Botão logar
        self.login_btn = QPushButton("Logar")
        self.login_btn.clicked.connect(self.try_login)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addLayout(password_layout)
        layout.addWidget(self.login_btn)

        self.setLayout(layout)

    def toggle_password_visibility(self, checked):
        if checked:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.toggle_password_btn.setText("Ocultar")
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.toggle_password_btn.setText("Mostrar")

    def try_login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        status,dados = backend.Auth(email,password)
        if status == 200:
            self.dadosToken = dados['access_token']
            self.open_datetime_window()
            print()
        else:
            QMessageBox.warning(self, "Erro", "Falha ao autenticar. Verifique suas credenciais.")

    def open_datetime_window(self):
        self.datetime_window = DateTimeWindow(self.dadosToken)
        self.datetime_window.show()
        self.close()


class DateTimeWindow(QWidget):
    def __init__(self,dadosToken):
        super().__init__()
        self.token = dadosToken
        self.setWindowTitle("Informe Data e Hora")

        label = QLabel("Escolha a data e hora:")

        # Widget para data e hora
        self.datetime_edit = QDateTimeEdit()
        self.datetime_edit.setCalendarPopup(True)
        self.datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.datetime_edit.setDateTime(self.datetime_edit.dateTime().currentDateTime())

        # Botão para confirmar
        self.confirm_btn = QPushButton("Confirmar")
        self.confirm_btn.clicked.connect(self.confirm_datetime)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.datetime_edit)
        layout.addWidget(self.confirm_btn)

        self.setLayout(layout)

    def confirm_datetime(self):
        dt = self.datetime_edit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        backend.point(self.token,dt)
        
        QMessageBox.information(self, "Data e Hora Selecionada", f"Você escolheu: {dt}")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
