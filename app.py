import customtkinter
from register import Register


class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        self.geometry("600x350")
        self.resizable(False, False)
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        frame = Register(container, self)

        self.frames[Register] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Register)

    def show_frame(self, type):
        frame = self.frames[type]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
