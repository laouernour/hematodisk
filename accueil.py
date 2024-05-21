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
        self.top_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=w, height=160, corner_radius=0)
        self.top_frame.place(x=0, y=0)
        label_text = Label(self.top_frame, text="Service Hématologie", font=('Karla', 48, 'bold'), bg="#28A0C6")
        label_text.place(x=750, y=60)
        self.ajouter_patient = ct.CTkButton(self.top_frame, text="+ Ajouter Patient", command=None, width=150, height=40,
                                            corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#EF3535',
                                            cursor='hand2', text_color='#FFFFFF')
        self.ajouter_patient.place(x=1100, y=108)

        self.ajouter_RV = ct.CTkButton(self.top_frame, text="+ Ajouter Rendez-vous", command=None, width=150,
                                            height=40,
                                            corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#2FC16A',
                                            cursor='hand2', text_color='#FFFFFF')
        self.ajouter_RV.place(x=890, y=108)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Resize to half the original size
        label_imageL = Label(self.top_frame, image=nouvelle_image, bg="#28A0C6")
        label_imageL.image = nouvelle_image  # Keep a reference to the image
        label_imageL.place(x=80, y=50)
        '''label_imageR = Label(self.top_frame, image=nouvelle_image, bg="#28A0C6")
        label_imageR.image = nouvelle_image  # Keep a reference to the image
        label_imageR.place(x=1760, y=6)'''



        # Left frame
        self.left_frame = ct.CTkFrame(self, fg_color='#28A0C6', width=250, height=h-50, corner_radius=0)
        self.left_frame.place(x=0, y=149)

        self.Liste_patient = ct.CTkButton(self.left_frame, text=" Liste des Patient", command=None, width=150,
                                       height=40,
                                       corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                       cursor='hand2', text_color='#FFFFFF')
        self.Liste_patient.place(x=25, y=50)
        self.Liste_RDV = ct.CTkButton(self.left_frame, text=" Liste des Rendez-vous ", command=None, width=150,
                                          height=40,
                                          corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                          cursor='hand2', text_color='#FFFFFF')
        self.Liste_RDV.place(x=25, y=120)
        self.reporter_RDV = ct.CTkButton(self.left_frame, text=" reporter Rendez-vous ", command=None, width=150,
                                      height=40,
                                      corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                      cursor='hand2', text_color='#FFFFFF')
        self.reporter_RDV.place(x=25, y=190)
        self.consultation = ct.CTkButton(self.left_frame, text=" Consultation ", command=None, width=150,
                                         height=40,
                                         corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                         cursor='hand2', text_color='#FFFFFF')
        self.consultation.place(x=25, y=260)
        self.stat = ct.CTkButton(self.left_frame, text=" Statistique ", command=None, width=150,
                                         height=40,
                                         corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                         cursor='hand2', text_color='#FFFFFF')
        self.stat.place(x=25, y=330)
        self.parametres = ct.CTkButton(self.left_frame, text=" Paramètres", command=None, width=150,
                                 height=40,
                                 corner_radius=15, font=('Karla', 16, 'bold'), fg_color="transparent",
                                 cursor='hand2', text_color='#FFFFFF')
        self.parametres.place(x=25, y=400)



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
