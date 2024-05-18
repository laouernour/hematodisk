import customtkinter as ct
from tkinter import *

class Accueil(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#263A5F')

        # Configure grid for the main window
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Top frame
        self.top_frame = ct.CTkFrame(self, fg_color='#18BDE1', height=200)
        self.top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=0, pady=0)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Resize to half the original size
        label_image = Label(self.top_frame, image=nouvelle_image, bg="#18BDE1")
        label_image.image = nouvelle_image  # Keep a reference to the image
        label_image.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        label_text = Label(self.top_frame, text="Hemato disk", font=('Karla', 26, 'bold'), bg="#18BDE1")
        label_text.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Left frame
        self.left_frame = ct.CTkFrame(self, fg_color='#18BDE1', width=250)
        self.left_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)

        # Center frame
        self.center_frame = ct.CTkFrame(self, fg_color='#ffffff', border_width=2, border_color='#263A5F')
        self.center_frame.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)




app = Accueil()
app.mainloop()
