import customtkinter
import main
from utils.variables import *

class Register(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        label = customtkinter.CTkLabel(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, text="Регістрація")

        label.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

        self.name_input = customtkinter.CTkEntry(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Ім'я")
        self.name_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

        self.nickname_input = customtkinter.CTkEntry(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Нікнейм")
        self.nickname_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

        self.password_input = customtkinter.CTkEntry(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Пароль", show="*")
        self.password_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

        button = customtkinter.CTkButton(
            master=self, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, text="Регістрація", command=self.register_callback)
        button.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

    def register_callback(self):
        name = self.name_input.get()
        nickname = self.nickname_input.get()
        password = self.password_input.get()

        main.register(name, nickname, password)
