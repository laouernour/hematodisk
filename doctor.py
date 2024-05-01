import tkinter as tk
import customtkinter as ct
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import pymysql


class Personne():
    def __init__(self, master):
        self.master = master
        self.formulaire_frame = ct.CTkFrame(master,  fg_color='#FFFFFF', border_width=2, border_color='#263A5F')
        self.formulaire_frame.grid()

        self.nom_label = ct.CTkLabel(self.formulaire_frame, text="Nom :", font=('Karla', 18))
        self.nom_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nom_entry = ct.CTkEntry(self.formulaire_frame, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.nom_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenom_label = ct.CTkLabel(self.formulaire_frame, text="Prénom :", font=('Karla', 18))
        self.prenom_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.prenom_entry = ct.CTkEntry(self.formulaire_frame, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.prenom_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        self.date_naissance_label = ct.CTkLabel(self.formulaire_frame, text="Date de Naissance :", font=('Karla', 18))
        self.date_naissance_label.grid(row=2, column=0, padx=20, pady=20,sticky="w")
        self.date_naissance_entry = ct.CTkEntry(self.formulaire_frame, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.date_naissance_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        self.wilaya_label = ct.CTkLabel(self.formulaire_frame, text="Wilaya :", font=('Karla', 18))
        self.wilaya_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.wilaya_entry = ct.CTkEntry(self.formulaire_frame, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.wilaya_entry.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        self.phone_nmbr_label = ct.CTkLabel(self.formulaire_frame, text="Téléphone:", font=('Karla', 18))
        self.phone_nmbr_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbr_entry = ct.CTkEntry(self.formulaire_frame, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.phone_nmbr_entry.grid(row=4, column=1, padx=20, pady=20, sticky="w")

        # Add other fields similarly

class Inscrire_doctor(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#263A5F')

        self.formulaire_frame2 = ct.CTkFrame(self,width=600,height=750,  fg_color='#FFFFFF', border_width=2, border_color='#263A5F', corner_radius=10)
        self.formulaire_frame2.pack()

        self.personne = Personne(self.formulaire_frame2)

        self.matricule_doctor_label = ct.CTkLabel(self.formulaire_frame2, text="Matricule Médecin:", font=('Karla', 18))
        self.matricule_doctor_label.grid(row=5, column=0, padx=20, pady=20,sticky="w")
        self.matricule_doctor_entry = ct.CTkEntry(self.formulaire_frame2, width=250, height=35, corner_radius=10, font=('Karla', 14))
        self.matricule_doctor_entry.grid(row=5, column=1, padx=20, pady=20, sticky="w")

        self.grad_label = ct.CTkLabel(self.formulaire_frame2, text="Grad:", font=('Karla', 18))
        self.grad_label.grid(row=6, column=0, padx=20, pady=20, sticky="w")

        grad = ["Généraliste", "Résident", "Assistant", "Maître Assistant", "Professeur"]
        self.grad_entry = ct.CTkComboBox(self.formulaire_frame2, values=grad,dropdown_font= ('Karla', 14),width=250, height=35, corner_radius=10,
                                         font=('Karla', 14),dropdown_fg_color='#FFFFFF')
        self.grad_entry.grid(row=6, column=1, padx=20, pady=20, sticky="w")

        self.enregistrer_doctor = ct.CTkButton(self.formulaire_frame2, text="Créer", command=None, width=150,
                                            height=40, corner_radius=15, font=('Karla', 18, 'bold'), fg_color='#263A5F',
                                            cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_doctor.grid(row=7, column=0, columnspan=2, pady=10)
        image_path = 'Hemato Desk logo.png'
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(2, 2)  # Redimensionne à la moitié de la taille originale
        label_image = Label(self.formulaire_frame2, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Garde une référence à l'image
        label_image.place(x=950, y=40)  # Ajustez la position selon vos besoins

# Create an instance of the custom window class and start the main loop
app = Inscrire_doctor()
app.mainloop()
