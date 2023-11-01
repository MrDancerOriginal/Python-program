import customtkinter
from utils.variables import *
import main


class Login(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        self.controller = controller

        label = customtkinter.CTkLabel(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, text="Login System", font=("Roboto", 24))

        label.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

        self.name_input = customtkinter.CTkEntry(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Ім'я")
        self.name_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

        self.password_input = customtkinter.CTkEntry(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Пароль", show="*")
        self.password_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

        self.button = customtkinter.CTkButton(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, text="Авторизація", command=self.login)
        self.button.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

    def login(self):
        name = self.name_input.get()
        password = self.password_input.get()

        main.login(name, password)
