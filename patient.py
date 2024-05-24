
import customtkinter as ct
from tkinter import *
from tkinter import messagebox
import pymysql

class Inscrire_patient(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire patient")
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

        # Nom and Prénom in the same row du patient
        self.nomP_label = ct.CTkLabel(self.inscription_frame, text="Nom :", font=('Karla', 16))
        self.nomP_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nomP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.nomP_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenomP_label = ct.CTkLabel(self.inscription_frame, text="Prénom :", font=('Karla', 16))
        self.prenomP_label.grid(row=0, column=2, padx=20, pady=20, sticky="w")
        self.prenomP_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.prenomP_entry.grid(row=0, column=3, padx=20, pady=20, sticky="w")

        # Date de Naissance
        self.date_naissanceP_label = ct.CTkLabel(self.inscription_frame, text="Date de Naissance :", font=('Karla', 16))
        self.date_naissanceP_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.date_naissanceP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.date_naissanceP_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Wilaya
        self.wilayaP_label = ct.CTkLabel(self.inscription_frame, text="Wilaya :", font=('Karla', 16))
        self.wilayaP_label.grid(row=1, column=2, padx=20, pady=20, sticky="w")
        self.wilayaP_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.wilayaP_entry.grid(row=1, column=3, padx=20, pady=20, sticky="w")

        # Téléphone
        self.phone_nmbrP_label = ct.CTkLabel(self.inscription_frame, text="Téléphone:", font=('Karla', 16))
        self.phone_nmbrP_label.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbrP_entry = ct.CTkEntry(self.inscription_frame, width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.phone_nmbrP_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

       # Matricule
        '''self.matricule_Patient_label = ct.CTkLabel(self.inscription_frame, text="Matricule Patient:", font=('Karla', 16))
        self.matricule_Patient_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        self.matricule_Patient_entry = ct.CTkEntry(self.inscription_frame,  width=200, height=30, corner_radius=10, font=('Karla', 14))
        self.matricule_Patient_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")'''

        # Matricule
        self.sexe_Patient_label = ct.CTkLabel(self.inscription_frame, text="Sexe :",
                                                   font=('Karla', 16))
        self.sexe_Patient_label.grid(row=2, column=2, padx=20, pady=20, sticky="w")
        sexe=['Homme','Femme']
        self.sexe_Patient_entry = ct.CTkComboBox(self.inscription_frame, width=200, height=30, corner_radius=10,values=sexe, dropdown_fg_color='#FFFFFF',
                                                   font=('Karla', 14))
        self.sexe_Patient_entry.grid(row=2, column=3, padx=20, pady=20, sticky="w")

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

        # Load the image

        image_path = 'Hemato Desk logo.png'  # Ensure this path is correct
        self.original_image = PhotoImage(file=image_path)
        nouvelle_image = self.original_image.subsample(3, 3)  # Resize to one-third of the original size

        # Create the Label with the image
        label_image = Label(self.label_frame, image=nouvelle_image, bg="white")
        label_image.image = nouvelle_image  # Keep a reference to the image to prevent garbage collection
        label_image.pack()

    def creer(self):
        if (self.nomP_entry.get() == "" or self.prenomP_entry.get() == "" or self.date_naissanceP_entry.get() == ""
                or self.wilayaP_entry.get() == "" or self.phone_nmbrP_entry.get() == ""
                or self.groupage_entry.get() == ""):
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        else:
            try:
                # Établir une connexion à la base de données
                con = pymysql.connect(host='localhost', user='root', password='', db='hematodisk_data_base')
                cur = con.cursor()

                # Récupération du matricule_administrateur à partir de la table administrateur
                cur.execute("SELECT matricule_administrateur FROM administrateur")
                matricule_administrateur = cur.fetchone()[0]

                # Insertion des données dans la table patient avec vérification de l'existence du matricule_administrateur
                cur.execute("""
                    INSERT INTO patient (nom, prenom, date_de_naissance, sexe, wilaya, telephone, groupage, antecedents,FKmatricule_administrateur) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                            (
                                self.nomP_entry.get(), self.prenomP_entry.get(),
                                self.date_naissanceP_entry.get(), self.sexe_Patient_entry.get(),
                                self.wilayaP_entry.get(), self.phone_nmbrP_entry.get(),
                                self.groupage_entry.get(), self.antecedents_entry.get(),
                                matricule_administrateur
                            ))

                # Committez les changements
                con.commit()
                messagebox.showinfo("Succès", "Inscription réussie", parent=self)
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'inscription : {str(e)}", parent=self)
                print(str(e))
            finally:
                # Fermez la connexion
                if con:
                    con.close()


# Create an instance of the Inscrire_patient class and start the main loop
app = Inscrire_patient()
app.mainloop()


