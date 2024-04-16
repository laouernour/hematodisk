import tkinter as tk
from tkinter import messagebox

def se_connecter():
    matricule = entry_matricule.get()
    mot_de_passe = entry_mot_de_passe.get()
    # Ici, vous pouvez ajouter la logique pour vérifier les identifiants
    messagebox.showinfo("Login", "Connexion réussie!")

# Création de la fenêtre principale
app = tk.Tk()
app.title('Bienvenue Sur Hematodesk')

# Configuration du fond avec des cellules sanguines (remplacer 'path_to_image' par le chemin de votre image)
background_image = tk.PhotoImage(file='background1.png')
background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Ajout du titre
label_titre = tk.Label(app, text="Bienvenue Sur Hematodesk", fg="white", bg="black")
label_titre.pack()

# Ajout des champs de saisie
label_matricule = tk.Label(app, text="Matricule :")
label_matricule.pack()
entry_matricule = tk.Entry(app)
entry_matricule.pack()

label_mot_de_passe = tk.Label(app, text="Mot de passe :")
label_mot_de_passe.pack()
entry_mot_de_passe = tk.Entry(app, show="*")
entry_mot_de_passe.pack()

# Ajout du bouton de connexion
bouton_connexion = tk.Button(app, text="Se Connecter", command=se_connecter)
bouton_connexion.pack()

# Ajout du lien pour mot de passe oublié
lien_mdp_oublie = tk.Label(app, text="Mot de passe oublié ?", fg="blue", cursor="hand2")
lien_mdp_oublie.pack()

# Lancement de l'application
app.mainloop()
