import customtkinter as ct
from tkinter import *
from tkinter import messagebox
import pymysql

class Inscrire_patient(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        self.geometry('850x500+300+100')
        self.configure(bg='#263A5F')

        self.formulaire_frame = ct.CTkFrame(self, fg_color='#FFFFFF', width=800, height=490, border_width=2,
                                            border_color='#263A5F',corner_radius= 0)
        self.formulaire_frame.pack(expand=True, fill='both')

        # Frame for the title label
        self.label_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.label_frame.pack(pady=2)

        self.label = ct.CTkLabel(self.label_frame, text="Inscrire Patient :", font=('Karla', 18, 'bold'))
        self.label.pack(expand=True, pady=10)

        # Frame for inscription form using grid
        self.inscription_frame = ct.CTkFrame(self.formulaire_frame, fg_color='#FFFFFF')
        self.inscription_frame.pack(pady=10)

        # Nom and Prénom in the same row
        self.nom_label = ct.CTkLabel(self.inscription_frame, text="Nom :", font=('Karla', 16))
        self.nom_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nom_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.nom_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenom_label = ct.CTkLabel(self.inscription_frame, text="Prénom :", font=('Karla', 16))
        self.prenom_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        self.prenom_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.prenom_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Date de Naissance
        self.date_naissance_label = ct.CTkLabel(self.inscription_frame, text="Date de Naissance :", font=('Karla', 16))
        self.date_naissance_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.date_naissance_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.date_naissance_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Wilaya
        self.wilaya_label = ct.CTkLabel(self.inscription_frame, text="Wilaya :", font=('Karla', 16))
        self.wilaya_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.wilaya_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.wilaya_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbr_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 16))
        self.phone_nmbr_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbr_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.phone_nmbr_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        # Matricule
        self.matricule_Patient_label = ct.CTkLabel(self.inscription_frame, text="Matricule Patient:", font=('Karla', 16))
        self.matricule_Patient_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        self.matricule_Patient_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.matricule_Patient_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")

        # Groupage
        self.groupage_label = ct.CTkLabel(self.inscription_frame, text="Groupage: ", font=('Karla', 16))
        self.groupage_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        groupage = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        self.groupage_entry = ct.CTkComboBox(self.inscription_frame, values=groupage, dropdown_font=('Karla', 14),  width=200, height=30, corner_radius=10, font=('Karla', 14), dropdown_fg_color='#FFFFFF')
        self.groupage_entry.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        # Antecedents
        self.antecedents_label = ct.CTkLabel(self.inscription_frame, text="Antécédents", font=('Karla', 16))
        self.antecedents_label.grid(row=3, column=2, padx=20, pady=20, sticky="w")
        self.antecedents_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.antecedents_entry.grid(row=3, column=3, padx=20, pady=20, sticky="w")

        # Button to Create Account
        self.enregistrer_patient = ct.CTkButton(self.inscription_frame, text="Créer", command=self.creer, width=250,
                                                height=40, corner_radius=15, font=('Karla', 16, 'bold'), fg_color='#263A5F',
                                                cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_patient.grid(row=4, column=1, columnspan=2, pady=8)

        # Image
        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(3, 3)  # Redimensionne à la moitié de la taille originale
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Garde une référence à l'image
        label_image.pack()  # Ajustez la position selon vos besoins
    def creer(self):
        if (self.nom_entry.get() == "" or self.prenom_entry.get() == "" or self.date_naissance_entry.get() == ""
                or self.wilaya_entry.get() == "" or self.phone_nmbr_entry.get() == ""
                or self.matricule_Patient_entry.get() == "" or self.groupage_entry.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()
                # Insert the data into your database (adjust the table name and columns as needed)
                cur.execute("INSERT INTO patients (nom, prenom, date_naissance, wilaya, telephone, matricule_patient, groupage, antecedents) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (self.nom_entry.get(), self.prenom_entry.get(), self.date_naissance_entry.get(),
                             self.wilaya_entry.get(), self.phone_nmbr_entry.get(), self.matricule_Patient_entry.get(),
                             self.groupage_entry.get(), self.antecedents_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Succès", "Inscription réussie", parent=self)
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)

# Create an instance of the Inscrire_patient class and start the main loop
app = Inscrire_patient()
app.mainloop()