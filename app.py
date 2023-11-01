import customtkinter
from login import Login
from register import Register

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        self.geometry("600x350")
        self.resizable(False, False)
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for Frame in (Login, Register):
            frame = Frame(container, self)

            self.frames[Frame] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, type):
        frame = self.frames[type]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
