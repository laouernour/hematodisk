import tkinter as tk
import customtkinter as ct

class personne():
    def __init__(self, master):

        self.formulaire_frame = ct.CTkFrame(master, width=800, height=500,fg_color='#FFFFFF')
        self.formulaire_frame.grid(row=0, column=0, padx=0, pady=0,sticky='')

        self.nom = ct.CTkLabel(self.formulaire_frame, text="Nom :", font=('Karla', 20))
        self.nom.grid(row=0, column=0, padx=20, pady=20,sticky="w")
        entry_nom = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10)
        entry_nom.grid(row=0, column=1, padx=20, pady=20,sticky="w")

        self.prenom = ct.CTkLabel(self.formulaire_frame, text="Prénom :", font=('Karla', 20))
        self.prenom.grid(row=1, column=0, padx=20, pady=20,sticky="w")
        entry_prenom = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10)
        entry_prenom.grid(row=1, column=1, padx=20, pady=20,sticky="w")

        self.date_naissance = ct.CTkLabel(self.formulaire_frame, text="Date de Naissance :", font=('Karla', 20))
        self.date_naissance.grid(row=2, column=0, padx=20, pady=20,sticky="w")
        entry_date_naissance = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10)
        entry_date_naissance.grid(row=2, column=1, padx=20, pady=20,sticky="w")

        self.wilaya = ct.CTkLabel(self.formulaire_frame, text="Wilaya :", font=('Karla', 20))
        self.wilaya.grid(row=3, column=0, padx=20, pady=20,sticky="w")
        entry_wilaya = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10)
        entry_wilaya.grid(row=3, column=1, padx=20, pady=20,sticky="w")

class Inscrire(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("S'inscrire")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure((0,1), weight=1)

        # Chargement de l'image de fond
        self.bg_image = tk.PhotoImage(file="background.png")

        # Création d'une étiquette pour l'image de fond et placement
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.formulaire_frame = ct.CTkFrame(self, width=800, height=500, fg_color='#FFFFFF')
        self.formulaire_frame.place(x=1,y=1)

        personne(self.formulaire_frame)

        self.matricule_ADM = ct.CTkLabel(self.formulaire_frame, text="Matricule :", font=('Karla', 20))
        self.matricule_ADM.grid(row=4, column=0, padx=40, pady=30,sticky="w")
        entry_matricule_ADM = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10)
        entry_matricule_ADM.grid(row=4, column=1, padx=40, pady=30,sticky="w")

        self.MP = ct.CTkLabel(self.formulaire_frame, text="Mot de passe :", font=('Karla', 20))
        self.MP.grid(row=5, column=0, padx=40, pady=20,sticky="w")
        entry_MP = ct.CTkEntry(self.formulaire_frame, width=300, height=40, corner_radius=10)
        entry_MP.grid(row=5, column=1, padx=40, pady=30,sticky="w")

# Création d'une instance de la classe de fenêtre personnalisée et démarrage de la boucle principale
app = Inscrire()
app.mainloop()
