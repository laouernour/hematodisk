import customtkinter as ct
from tkinter import PhotoImage, Label

class Accueil(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#263A5F')

        # Top frame
        self.top_frame = ct.CTkFrame(self, fg_color='#18BDE1', width=w, height=150)
        self.top_frame.place(x=0, y=0)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Resize to half the original size
        label_imageL = Label(self.top_frame, image=nouvelle_image, bg="#18BDE1")
        label_imageL.image = nouvelle_image  # Keep a reference to the image
        label_imageL.place(x=20, y=10)
        label_imageR = Label(self.top_frame, image=nouvelle_image, bg="#18BDE1")
        label_imageR.image = nouvelle_image  # Keep a reference to the image
        label_imageR.place(x=1700, y=10)

        label_text = Label(self.top_frame, text="Hemato disk", font=('Karla', 48, 'bold'), bg="#18BDE1")
        label_text.place(x=750, y=60)

        # Left frame
        self.left_frame = ct.CTkFrame(self, fg_color='#18BDE1', width=250, height=h-150)
        self.left_frame.place(x=0, y=149)

        # Center frame
        self.center_frame = ct.CTkScrollableFrame(self, fg_color='#ffffff', border_width=2, border_color='#263A5F', width=w-280, height=h-150)
        self.center_frame.place(x=250, y=149)

if __name__ == "__main__":
    app = Accueil()
    app.mainloop()
