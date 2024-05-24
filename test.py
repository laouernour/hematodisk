import customtkinter

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, parent):  # Add parent as an argument
        super().__init__(parent)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")

        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # Pass self as an argument
        else:
            self.toplevel_window.focus()  # if window exists focus it

app = App()
app.mainloop()
