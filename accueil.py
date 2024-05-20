import customtkinter as ct
from tkinter import PhotoImage, Label

class Accueil(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#78BDCC')

        # Top frame
        self.top_frame = ct.CTkFrame(self, fg_color='#78BDCC', width=w, height=160, corner_radius=0)
        self.top_frame.place(x=0, y=0)
        self.ajouter_patient = ct.CTkButton(self.top_frame, text="ajouter patient", command=None, width=150, height=40,
                                         corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#263A5F',
                                         cursor='hand2', text_color='#FFFFFF')
        self.ajouter_patient.place(x=1000, y=100)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(3, 3)  # Resize to half the original size
        label_imageL = Label(self.top_frame, image=nouvelle_image, bg="#78BDCC")
        label_imageL.image = nouvelle_image  # Keep a reference to the image
        label_imageL.place(x=20, y=10)
        label_imageR = Label(self.top_frame, image=nouvelle_image, bg="#78BDCC")
        label_imageR.image = nouvelle_image  # Keep a reference to the image
        label_imageR.place(x=1700, y=10)

        label_text = Label(self.top_frame, text="Service Hématologie ", font=('Karla', 48, 'bold'), bg="#78BDCC")
        label_text.place(x=750, y=60)

        # Left frame
        self.left_frame = ct.CTkFrame(self, fg_color='#78BDCC', width=250, height=h-50, corner_radius=0)
        self.left_frame.place(x=0, y=149)


        # Center frame
        self.center_frame = ct.CTkScrollableFrame(self, fg_color='#ffffff', border_width=2, border_color='#263A5F', width=w-279, height=h-160,corner_radius=0)
        self.center_frame.place(x=250, y=150)

if __name__ == "__main__":
    app = Accueil()
    app.mainloop()
