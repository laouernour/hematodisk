import customtkinter as ct
from tkinter import messagebox
class Personne():
    def __init__(self, master):

        self.formulaire_frame = ct.CTkFrame(master, width=900, height=500, fg_color='#FFFFFF', border_width=2, border_color='#263A5F')
        self.formulaire_frame.grid()

        self.nom = ct.CTkLabel(self.formulaire_frame, text="Nom :", font=('Karla', 20))
        self.nom.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        entry_nom = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        entry_nom.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.prenom = ct.CTkLabel(self.formulaire_frame, text="Prénom :", font=('Karla', 20))
        self.prenom.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        entry_prenom = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        entry_prenom.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        self.date_naissance = ct.CTkLabel(self.formulaire_frame, text="Date de Naissance :", font=('Karla', 20))
        self.date_naissance.grid(row=2, column=0, padx=20, pady=20,sticky="w")
        entry_date_naissance = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        entry_date_naissance.grid(row=2, column=1, padx=20, pady=20, sticky="w")

        self.wilaya = ct.CTkLabel(self.formulaire_frame, text="Wilaya :", font=('Karla', 20))
        self.wilaya.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        entry_wilaya = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        entry_wilaya.grid(row=3, column=1, padx=20, pady=20, sticky="w")

        self.phone_nmbr = ct.CTkLabel(self.formulaire_frame, text="Téléphone:", font=('Karla', 20))
        self.phone_nmbr.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        entry_phone_nmbr = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10, font=('Karla', 16))
        entry_phone_nmbr.grid(row=4, column=1, padx=20, pady=20, sticky="w")

class Inscrire(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))
        self.configure(bg='#263A5F')


        #self.grid_rowconfigure(0, weight=1)  # configure grid system
        #self.grid_columnconfigure(0, weight=1)

        self.formulaire_frame1 = ct.CTkFrame(self, width=900, height=600, fg_color='#FFFFFF', border_width=2, border_color='#263A5F', corner_radius=10)
        self.formulaire_frame1.pack(expand=True)
# stocker l'instance  de la classe Personne
        self.personne=Personne(self.formulaire_frame1)


        self.matricule_ADM = ct.CTkLabel(self.formulaire_frame1, text="Matricule :", font=('Karla', 20))
        self.matricule_ADM.grid(row=5, column=0, padx=20, pady=30,sticky="w")
        entry_matricule_ADM = ct.CTkEntry(self.formulaire_frame1, width=300, height=40, corner_radius=10, font=('Karla', 16))
        entry_matricule_ADM.grid(row=5, column=1, padx=40, pady=30, sticky="w")

        self.MP = ct.CTkLabel(self.formulaire_frame1, text="Mot de passe :", font=('Karla', 20))
        self.MP.grid(row=6, column=0, padx=20, pady=20, sticky="w")
        entry_MP = ct.CTkEntry(self.formulaire_frame1, show="*", width=300, height=40, corner_radius=10, font=('Karla', 16))
        entry_MP.grid(row=6, column=1, padx=40, pady=20, sticky="w")

        self.confirmation_MP = ct.CTkLabel(self.formulaire_frame1, text="Mot de passe :", font=('Karla', 20))
        self.confirmation_MP.grid(row=7, column=0, padx=20, pady=20, sticky="w")
        entry_confirmation_MP = ct.CTkEntry(self.formulaire_frame1,show="*", width=300, height=40, corner_radius=10, font=('Karla', 16))
        entry_confirmation_MP.grid(row=7, column=1, padx=40, pady=20, sticky="w")

        self.enregistrer_ADM= ct.CTkButton(self.formulaire_frame1, text="Créer", width=150, height=40, corner_radius=15, font=('Karla', 20, 'bold'),fg_color='#263A5F', cursor='hand2', text_color='#FFFFFF')
        self.enregistrer_ADM.grid(row=8, column=0)
        self.enregistrer_ADM.configure(command=self.creer)

#----------------------------------------
        #connction avec la base de donnée
    def creer(self):
        personne_instance = personne(self.formulaire_frame1)  # Créer une instance de la classe personne
        if personne_instance.entry_nom.get() == "" or personne_instance.entry_prenom.get() == "" or personne_instance.entry_date_naissance.get() == "" or personne_instance.entry_wilaya.get() == "" or personne_instance.entry_phone_nmbr.get() == "" or self.entry_matricule_ADM.get() == "" or self.entry_MP.get() == "" or self.entry_confirmation_MP.get() == "":
            messagebox.showerror("Erreur", "Inscription incomplète", parent=self)
        elif self.entry_MP.get() != self.entry_confirmation_MP.get():
            messagebox.showerror("Erreur", "Les mots de passe ne sont pas conformes", parent=self)
        else:
            try:
                pass
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion : {str(es)}", parent=self)


# Création d'une instance de la classe de fenêtre personnalisée et démarrage de la boucle principale
app = Inscrire()
app.mainloop()