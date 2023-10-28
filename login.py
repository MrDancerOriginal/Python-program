import customtkinter
from utils.variables import *
import main
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

rt = customtkinter.CTk()

rt.geometry("600x350")


def login():
    name = name_input.get()
    password = password_input.get()

    main.login(name, password)


fr = customtkinter.CTkFrame(master=rt)
fr.pack(pady=40, padx=120, fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, text="Login System", font=("Roboto", 24))
label.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

name_input = customtkinter.CTkEntry(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Ім'я")
name_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

password_input = customtkinter.CTkEntry(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, placeholder_text="Пароль", show="*")
password_input.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

button = customtkinter.CTkButton(
    master=fr, width=DEFAULT_INPUT_WIDTH, height=DEFAULT_INPUT_HEIGHT, text="Авторизація", command=login)
button.pack(pady=DEFAULT_PADY, padx=DEFAULT_PADX)

rt.mainloop()
