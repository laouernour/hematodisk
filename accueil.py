import customtkinter as ct
from tkinter import PhotoImage, Label
from tkinter import ttk

class Accueil(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Accueil")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#78BDCC')

        # Top frame
        self.top_frame = ct.CTkFrame(self, fg_color='#78BDCC', width=w, height=160, corner_radius=0)
        self.top_frame.place(x=0, y=0)
        self.ajouter_patient = ct.CTkButton(self.top_frame, text="+ Ajouter Patient", command=None, width=150, height=40,
                                            corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#263A5F',
                                            cursor='hand2', text_color='#FFFFFF')
        self.ajouter_patient.place(x=1350, y=108)

        self.ajouter_RV = ct.CTkButton(self.top_frame, text="+ Ajouter Rendez-vous", command=None, width=150,
                                            height=40,
                                            corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#263A5F',
                                            cursor='hand2', text_color='#FFFFFF')
        self.ajouter_RV.place(x=1140, y=108)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(3, 3)  # Resize to half the original size
        label_imageL = Label(self.top_frame, image=nouvelle_image, bg="#78BDCC")
        label_imageL.image = nouvelle_image  # Keep a reference to the image
        label_imageL.place(x=20, y=6)
        label_imageR = Label(self.top_frame, image=nouvelle_image, bg="#78BDCC")
        label_imageR.image = nouvelle_image  # Keep a reference to the image
        label_imageR.place(x=1760, y=6)

        label_text = Label(self.top_frame, text="Service Hématologie", font=('Karla', 48, 'bold'), bg="#78BDCC")
        label_text.place(x=750, y=60)

        # Left frame
        self.left_frame = ct.CTkFrame(self, fg_color='#78BDCC', width=250, height=h-50, corner_radius=0)
        self.left_frame.place(x=0, y=149)

        # Center frame
        self.center_frame = ct.CTkScrollableFrame(self, fg_color='#ffffff', border_width=2, border_color='#263A5F', width=w-279, height=h-160, corner_radius=0)
        self.center_frame.place(x=250, y=150)

        # Style for Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", background="#ffffff", foreground="black", fieldbackground="#ffffff")
        style.map("Custom.Treeview", background=[('selected', '#78BDCC')], foreground=[('selected', 'black')])

        # Treeview Table
        columns = ('Matricule', 'Nom', 'Prénom', 'Age', 'Groupage')
        self.treeview = ttk.Treeview(self.center_frame, columns=columns, show='headings', style="Custom.Treeview")
        self.treeview.pack(expand=True, fill='both')

        # Define headings
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, anchor='center', width=100)

        # Add some sample data
        self.treeview.insert('', 'end', values=('12345', 'Doe', 'John', '30', 'A+'))
        self.treeview.insert('', 'end', values=('67890', 'Smith', 'Anna', '25', 'B+'))

if __name__ == "__main__":
    app = Accueil()
    app.mainloop()
