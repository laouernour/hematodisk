import customtkinter as ct
from tkinter import messagebox
import pymysql

class Personne():
    def __init__(self, master):
        self.master = master
        self.formulaire_frame = ct.CTkFrame(master,  fg_color='#FFFFFF', border_width=2, border_color='#263A5F')
        self.formulaire_frame.grid()

        self.nom_label = ct.CTkLabel(self.formulaire_frame, text="Nom :", font=('Karla', 20))
        self.nom_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.nom_entry = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        self.nom_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenom_label = ct.CTkLabel(self.formulaire_frame, text="Prénom :", font=('Karla', 20))
        self.prenom_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.prenom_entry = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        self.prenom_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        self.date_naissance_label = ct.CTkLabel(self.formulaire_frame, text="Date de Naissance :", font=('Karla', 20))
        self.date_naissance_label.grid(row=2, column=0, padx=20, pady=20,sticky="w")
        self.date_naissance_entry = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        self.date_naissance_entry.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        self.wilaya_label = ct.CTkLabel(self.formulaire_frame, text="Wilaya :", font=('Karla', 20))
        self.wilaya_label.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        self.wilaya_entry = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        self.wilaya_entry.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        self.phone_nmbr_label = ct.CTkLabel(self.formulaire_frame, text="Téléphone:", font=('Karla', 20))
        self.phone_nmbr_label.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        self.phone_nmbr_entry = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        self.phone_nmbr_entry.grid(row=4, column=1, padx=20, pady=20, sticky="w")

class Inscrire(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#263A5F')

        self.formulaire_frame1 = ct.CTkFrame(self, width=500, height=500, fg_color='#FFFFFF', border_width=2, border_color='#263A5F', corner_radius=10)
        self.formulaire_frame1.pack(expand=True)

        self.personne = Personne(self.formulaire_frame1)

        self.matricule_ADM_label = ct.CTkLabel(self.formulaire_frame1, text="Matricule :", font=('Karla', 20))
        self.matricule_ADM_label.grid(row=5, column=0, padx=20, pady=20,sticky="w")
        self.matricule_ADM_entry = ct.CTkEntry(self.formulaire_frame1, width=300, height=40, corner_radius=10, font=('Karla', 16))
        self.matricule_ADM_entry.grid(row=5, column=1, padx=20, pady=20, sticky="w")

        self.MP_label = ct.CTkLabel(self.formulaire_frame1, text="Mot de passe :", font=('Karla', 20))
        self.MP_label.grid(row=6, column=0, padx=20, pady=20, sticky="w")
        self.MP_entry = ct.CTkEntry(self.formulaire_frame1, show="*", width=300, height=40, corner_radius=10, font=('Karla', 16))
        self.MP_entry.grid(row=6, column=1, padx=20, pady=20, sticky="w")

        self.confirmation_MP_label = ct.CTkLabel(self.formulaire_frame1, text="Confirmation du mot de passe :", font=('Karla', 20))
        self.confirmation_MP_label.grid(row=7, column=0, padx=20, pady=20, sticky="w")
        self.confirmation_MP_entry = ct.CTkEntry(self.formulaire_frame1,show="*", width=300, height=40, corner_radius=10, font=('Karla', 16))
        self.confirmation_MP_entry.grid(row=7, column=1, padx=20, pady=20, sticky="w")

        self.enregistrer_ADM= ct.CTkButton(self.formulaire_frame1, text="Créer", command=self.creer, width=150, height=40, corner_radius=15, font=('Karla', 20, 'bold'), fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_ADM.grid(row=7, columnspan=2, pady=20)

    def creer(self):
        if self.personne.nom_entry.get() == "" or self.personne.prenom_entry.get() == "" or self.personne.date_naissance_entry.get() == "" or self.personne.wilaya_entry.get() == "" or self.personne.phone_nmbr_entry.get() == "" or self.matricule_ADM_entry.get() == "" or self.MP_entry.get() == "" or self.confirmation_MP_entry.get() == "":
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        elif self.MP_entry.get() != self.confirmation_MP_entry.get():
            messagebox.showerror("Erreur", "Les mots de passe ne sont pas conformes", parent=self)
        else:
            try:
                # Connecter à la base de données et traiter l'inscription ici
                con=pymysql.connect(host='localhost',user='root',password='',db='hematodisk_data_base')
                cur=con.cursor()
                cur.execute("select * fe")
                pass
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)

# Création d'une instance de la classe Inscrire et démarrage de la boucle principale
app = Inscrire()
app.mainloop()
