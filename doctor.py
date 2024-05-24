import customtkinter as ct
from tkinter import *
from tkinter import messagebox
import pymysql

class Inscrire(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#263A5F')

        self.formulaire_frame = ct.CTkFrame(self, fg_color='#FFFFFF', width=w, height=h, border_width=2,
                                            border_color='#263A5F')
        self.formulaire_frame.pack(expand=True, fill='both')

        # Frame for the title label
        self.label_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.label_frame.pack(pady=10)

        self.label = ct.CTkLabel(self.label_frame, text="Inscrire Doctor :", font=('Karla', 26,'bold'))
        self.label.pack(expand=True, pady=20)

        # Frame for inscription form using grid
        self.inscription_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.inscription_frame.pack(pady=10)

        # Nom and Prénom in the same row
        self.nom_label = ct.CTkLabel(self.inscription_frame, text="Nom :", font=('Karla', 18))
        self.nom_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nom_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.nom_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenom_label = ct.CTkLabel(self.inscription_frame, text="Prénom :", font=('Karla', 18))
        self.prenom_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        self.prenom_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                        font=('Karla', 14))
        self.prenom_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Date de Naissance
        self.date_naissance_label = ct.CTkLabel(self.inscription_frame, text="Date de Naissance :", font=('Karla', 18))
        self.date_naissance_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.date_naissance_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                                font=('Karla', 14))
        self.date_naissance_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Wilaya
        self.wilaya_label = ct.CTkLabel(self.inscription_frame, text="Wilaya :", font=('Karla', 18))
        self.wilaya_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.wilaya_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                        font=('Karla', 14))
        self.wilaya_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbr_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 18))
        self.phone_nmbr_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbr_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                            font=('Karla', 14))
        self.phone_nmbr_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Matricule
        self.matricule_doctor_label = ct.CTkLabel(self.inscription_frame, text="Matricule Médecin:", font=('Karla', 18))
        self.matricule_doctor_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        self.matricule_doctor_entry = ct.CTkEntry(self.inscription_frame, width=250, height=35, corner_radius=10,
                                                  font=('Karla', 14))
        self.matricule_doctor_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")

        # Grad
        self.grad_label = ct.CTkLabel(self.inscription_frame, text="Grade:", font=('Karla', 18))
        self.grad_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        grad = ["Généraliste", "Résident", "Assistant", "Maître Assistant", "Professeur"]
        self.grad_entry = ct.CTkComboBox(self.inscription_frame, values=grad, dropdown_font=('Karla', 14), width=250,
                                         height=35, corner_radius=10,
                                         font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.grad_entry.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        # Button to Create Account
        self.enregistrer_doctor = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250,
                                            height=40, corner_radius=15, font=('Karla', 18, 'bold'), fg_color='#263A5F',
                                            cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_doctor.grid(row=5, column=1, columnspan=2, pady=10)

        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Redimensionne à la moitié de la taille originale
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Garde une référence à l'image
        label_image.pack()  # Ajustez la position selon vos besoins

    def creer(self):
        if (self.nom_entry.get() == "" or self.prenom_entry.get() == "" or self.date_naissance_entry.get() == ""
                or self.wilaya_entry.get() == "" or self.phone_nmbr_entry.get() == ""
                or self.matricule_doctor_entry.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            # Placeholder for database connection and operation
            try:
                mydb = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                mycursor = mydb.cursor()
                mycursor.execute("insert into medecin (matricule_medecin,nom,prenom,date_de_naissance,wilaya,telephone,grade)values(%s,%s,%s,%s,%s,%s,%s)",
                                 (
                                 self.matricule_doctor_entry.get(),
                                 self.nom_entry.get(),
                                 self.prenom_entry.get(),
                                 self.date_naissance_entry.get(),
                                 self.wilaya_entry.get(),
                                 self.phone_nmbr_entry.get(),
                                 self.grad_entry.get(),
                ))
                messagebox.showinfo("Suuccess",f"Médecin enregistrer", parent=self )
                mydb.commit()
                mydb.close
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)


# Create an instance of the Inscrire class and start the main loop
app = Inscrire()
app.mainloop()