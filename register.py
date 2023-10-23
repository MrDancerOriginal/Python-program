import customtkinter
import main
from utils.variables import *


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def register_callback():
    name = name_input.get()
    nickname = nickname_input.get()
    password = password_input.get()

    main.register(name, nickname, password)


rt = customtkinter.CTk()

rt.geometry("800x550")


fr = customtkinter.CTkFrame(master=rt)

fr.pack(pady=30, padx=120, fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, text="Регістрація")
label.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

name_input = customtkinter.CTkEntry(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Ім'я")
name_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

nickname_input = customtkinter.CTkEntry(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Нікнейм")
nickname_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

password_input = customtkinter.CTkEntry(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Пароль", show="*")
password_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

button = customtkinter.CTkButton(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, text="Регістрація", command=register_callback)
button.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

rt.mainloop()
